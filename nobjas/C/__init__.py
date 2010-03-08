from nobjas import M
from nobjas.util import tmpl

from google.appengine.ext import webapp
from google.appengine.api import users

# submodule list
__all__=['Root','Topic', 'Comment']

class CBase():
    def __init__(self, handler):
        self.users    = users
        self.M        = M
        self.tmpl     = tmpl
        self.handler  = handler
        self.request  = handler.request
        self.response = handler.response
