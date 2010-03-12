# -*- coding: utf-8 -*-
from nobjas.C import CBase

class add(CBase):
    def        get(self): self._get()
    def mobile_get(self): self._get()
    def       _get(self):
        topic_key = self.request.get('id')

        self.tmpl.filename( 'comment/add.html' )
        self.tmpl.set(
            topic_key=topic_key,
        )
        self.tmpl.render()

    def        post(self): self._post()
    def mobile_post(self): self._post()
    def       _post(self):
        comment = self.M.Comments()
        key     = self.request.get('id')

        topic = self.M.Topics().find(key)
        comment.topic = topic.key()
        comment.body  = self.request.get('body')

        if self.users.get_current_user():
            comment.user = self.users.get_current_user()

        comment.put()
        self.handler.redirect('/topic/view?id=' + key)

