# -*- coding: utf-8 -*-
from nobjas.C import CBase

class add(CBase):
    def        post(self): self._post()
    def mobile_post(self): self._post()
    def       _post(self):
        category = self.M.Categories()

        category.title        = self.request.get('title')
        category.description  = self.request.get('description')
        self.handler.redirect('/')
