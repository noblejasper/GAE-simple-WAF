from nobjas import M
from nobjas.util import tmpl

from google.appengine.ext import webapp
from google.appengine.api import users

# submodule list
__all__=['Root',]

class CBase(webapp.RequestHandler):
    def __init__(self):
        self.users = users
        self.M     = M
        self.tmpl  = tmpl
