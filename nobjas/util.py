import os
from google.appengine.ext.webapp import template

# import logging
# logging.getLogger().setLevel(logging.DEBUG)
# logging.debug(message)

class tmpl():
    def __init__( self, instance, filename=None ):
        self.filename        = filename
        self.response        = instance.response
        self.values          = {}
        self.path            = '../app/templates/' + self.filename

    def filename( self, filename=None ):
        if filename:
            self.filename = filename
        return self.filename

    def set( self, **values ):
        for k,v in values.items():
            self.values[k] = v

    def render(self):
        self.path = os.path.join(os.path.dirname(__file__), self.path)
        self.response.out.write(
            template.render(self.path, self.values)
        )
