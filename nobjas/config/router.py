from google.appengine.ext import webapp

from nobjas.C import *

class router():
    def __init__(self):
        self.application = webapp.WSGIApplication(
            [
                ('/',     Root.index),
                ('/sign', Root.guestbook)
                ],
            debug=True
        )
