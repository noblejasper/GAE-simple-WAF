# -*- coding: utf-8 -*-
from nobjas.C import CBase

class error404(CBase):
    def get(self):
        self._404()
    def post(self):
        self._404()
    def head(self):
        self._404()
    def options(self):
        self._404()
    def put(self):
        self._404()
    def delete(self):
        self._404()
    def trace(self):
        self._404()

    def mobile_get(self):
        self._mobile_404()
    def mobile_post(self):
        self._mobile_404()
    def mobile_head(self):
        self._mobile_404()
    def mobile_options(self):
        self._mobile_404()
    def mobile_put(self):
        self._mobile_404()
    def mobile_delete(self):
        self._mobile_404()
    def mobile_trace(self):
        self._mobile_404()

    def _404(self):
        self.response.set_status(404)
        self.tmpl.filename( 'error/404.html' )
        self.tmpl.render()

    def _mobile_404(self):
        self.response.set_status(404)
        self.tmpl.filename( 'error/404.html' )
        self.tmpl.render()
