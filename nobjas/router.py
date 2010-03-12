# -*- coding: utf-8 -*-
import re
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import login_required

from uamobile import detect
from nobjas.C import Error
from app.C import *

class router():
    def __init__(self):
        self.application = self.setup_application()

    def setup_application(self):
        return webapp.WSGIApplication(
            [(r'.*', RequestHandler)],
            debug=True
        )

class RequestHandler(webapp.RequestHandler):

    @login_required
    def get(self, *args):
        self._handle_request('get')
    def post(self, *args):
        self._handle_request('post')
    def head(self, *args):
        self._handle_request('head')
    def options(self, *args):
        self._handle_request('options')
    def put(self, *args):
        self._handle_request('put')
    def delete(self, *args):
        self._handle_request('delete')
    def trace(self, *args):
        self._handle_request('trace')
    def _handle_request(self, method):
        """全てのメソッドは全てdispatchに一度なげる"""
        dispatcher(self).dispatch(method)

class dispatcher():
    route = {}

    def __init__(self, handler):
        self.handler             = handler
        self.route['controller'] = 'root'
        self.route['action']     = 'index'
        self.device              = self.check_device()

    def dispatch(self,method):
        if self.get_route():
            controller   = self.create_controller_instance()
            if not self.dispatch_action(controller, method):
                # None dispatch
                self._404error()
        else:
            # None Controller
            self._404error()

    def get_route(self):
        path = self.handler.request.path

        if path == '/' :
            return True

        # special routing
        # WISH: read config yaml
        special_route = {
            '/copyright': ['root', 'index'],
        }

        if special_route.has_key(path):
            self.route['controller'] = special_route[path].pop(0)
            self.route['action']     = special_route[path].pop(0)
            return True

        matches = re.search('^/(\w+)/(\w+)', path)
        if matches:
            self.route['controller'] = matches.group(1)
            self.route['action'] = matches.group(2)
            return True
        else:
            return None

    def create_controller_instance(self):
        try:
            controller = eval(
                self.route['controller'].capitalize() + '.' + self.route['action']
                )

        except AttributeError:
            return None

        else:
            return controller(self.handler)

    def dispatch_action( self, controller=None, method="get" ):
        if controller:
            action_method = getattr(controller, method, None)
            if action_method:
                action_method()
                return True
            else:
                # None method of Controller
                return None
        else:
            # None Controller instance
            return None

    def _404error(self):
        self.route['controller'] = 'error'
        self.route['action']     = 'error404'
        controller   = self.create_controller_instance()
        self.dispatch_action(controller, 'get')

    def check_device(self):
        return detect(self.handler.request.environ)
