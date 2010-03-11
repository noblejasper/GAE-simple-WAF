import re
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import login_required

import JPmobile
from app.C import *

class router():
    def __init__(self):
        self.application = self.setup_application()

    def setup_application(self):
        return webapp.WSGIApplication(
            [(r'.*', RequestHandler)],
            debug=True
        )

class dispatcher():
    route = {}
    handler = ''

    def __init__(self, handler):
        self.handler             = handler
        self.route['controller'] = 'root'
        self.route['action']     = 'index'

    def dispatch(self,method):
        if self.get_route():
            self.check_device()
            controller   = self.create_controller_instance()
            self.dispatch_action(controller, method)
        else:
            # None Controller
            webapp.Response().set_status(404)

    def dispatch_action( self, controller=None, method="get" ):
        if controller:
            action_method = getattr(controller, method, None)
            if action_method:
                action_method()
            else:
                # None method of Controller
                webapp.Response().set_status(404)
        else:
            # None Controller instance
            webapp.Response().set_status(404)

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

    def check_device(self):
        self.is_mobile = JPmobile.is_mobile(self.handler.request.environ['HTTP_USER_AGENT'])
        return True

    def create_controller_instance(self):
        controller = eval(
            self.route['controller'].capitalize() + '.' + self.route['action']
        )
        return controller(self.handler)

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
        dispatcher(self).dispatch(method)
