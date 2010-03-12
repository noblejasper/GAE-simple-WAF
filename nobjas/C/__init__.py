# -*- coding: utf-8 -*-
from app import M
from nobjas.util import tmpl

from google.appengine.ext import webapp
from google.appengine.api import users

class CBase():
    def __init__(self, handler, device):
        self.users    = users
        self.M        = M
        self.request  = handler.request
        self.response = handler.response
        self.handler  = handler
        self.device   = device
        self.tmpl     = tmpl(self)
