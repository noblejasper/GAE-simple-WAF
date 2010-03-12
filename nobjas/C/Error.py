from nobjas.C import CBase

class error404(CBase):
    def get(self):
        self._404()
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

    def _404(self):
        self.response.set_status(404)
        template = self.tmpl( self, 'error/404.html' )
        template.render()
