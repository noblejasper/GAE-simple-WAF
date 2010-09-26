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
        categories = self.M.Category().find_all()
        count  = 0
        def _txn(array, name):
            result = False
            count  = 0
            for a in array:
                if a['name'] == name:
                    result = True
                    break
                count += 1
            return result, count
        result = []
        for cat in categories:
            if cat.parent_category:
                has_value, count = _txn(result, cat.parent_category.name)
                if has_value:
                    result[count]['child'].append({ 'name' : cat.name, 'key' :cat.key() })
                else:
                    result.append({
                        'name'  : cat.parent_category.name,
                        'key'   : cat.parent_category.key(),
                        'child' : [{ 'name' : cat.name, 'key' : cat.key() }],
                    })
            else:
                has_value, count = _txn(result, cat.name)
                if not has_value:
                    result.append({ 'name' : cat.name, 'key' :cat.key(), 'child' : [] })
        self.tmpl.set(
            categories = result,
        )

    def show_404(self):
        self.response.set_status(404)
        self.tmpl.filename('error/404.html')
        self.tmpl.render()
