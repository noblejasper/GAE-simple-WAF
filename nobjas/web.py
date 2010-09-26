# -*- coding: utf-8 -*-
import sys
import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from nobjas.router import router

class web():
    def __init__(self, path):
        self.router = router()
        # path append
        sys.path.append( os.path.join(os.path.abspath(os.path.dirname(path)), 'app/C') )

    def main(self):
        run_wsgi_app(self.router.application)

    def run(self):
        self.main()
