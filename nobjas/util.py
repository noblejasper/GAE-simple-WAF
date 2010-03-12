# -*- coding: utf-8 -*-
import os
from google.appengine.ext.webapp import template

# import logging
# logging.getLogger().setLevel(logging.DEBUG)
# logging.debug(message)

class tmpl():
    def __init__( self, instance, filename='' ):
        self._filename = filename
        self.response  = instance.response
        self.device    = instance.device
        self.values    = {}
        self.path      = '../app/templates/'

    def filename( self, filename='' ):
        if filename:
            self._filename = filename
        return self._filename

    def set( self, **values ):
        for k,v in values.items():
            self.values[k] = v

    def render(self):
        if not self._filename:
            raise 'NoTemplateFilename'
        if not self.device.is_nonmobile():
            # root/index.html -> root/mobile_index.html
            self._filename = os.path.dirname(self._filename) + '/mobile_' + os.path.basename(self._filename)
        path = self.path + self._filename
        path = os.path.join(os.path.dirname(__file__), path)
        self.response.out.write(
            template.render(path, self.values)
        )
