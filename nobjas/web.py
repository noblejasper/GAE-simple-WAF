from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from nobjas.router import router

class web():
    def __init__(self):
        self.router = router()

    def main(self):
        run_wsgi_app(self.router.application)

    def run(self):
        self.main()
