import re
from google.appengine.ext import webapp

from nobjas.C import *

class router():
    def __init__(self):
        self.application = self.setup_application()

    def setup_application(self):
        return webapp.WSGIApplication(
            [(r'.*', RequestHandler)],
            debug=True
        )

class dispatcher():
    def __init__(self, handler):
        self.handler = handler

    def dispatch(self,method):
        path       = self.handler.request.path
        route      = self.get_route(path)
        controller = self.create_controller_instance(route)
        self.dispatch_action(controller, method)

    def dispatch_action( self, controller=None, method="get" ):
        if controller:
            action_method = getattr(controller, method, None)
            if action_method:
                action_method()
            else:
                webapp.Response.set_status(404)
        else:
            webapp.Response.set_status(404)

    def get_route(self,path):
        route = {}
        if path == '/' :
            route['controller'] = 'root'
            route['action'] = 'index'
            return route

        # TODO: make special routing

        matches = re.search('^/(\w+)/(\w+)', path)
        if matches:
            route['controller'] = matches.group(1)
            route['action'] = matches.group(2)
        else:
            raise Exception('tenuki desu')

        return route

    def create_controller_instance(self,route):
        controller = eval( route['controller'].capitalize() + '.' + route['action'] )
        import logging
        logging.getLogger().setLevel(logging.DEBUG)
        logging.debug(controller)
        return controller(self.handler)

class RequestHandler(webapp.RequestHandler):
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
