# -*- coding: utf-8 -*-
from nobjas.C import CBase

class view(CBase):
    def        get(self): self._get()
    def mobile_get(self): self._get()
    def       _get(self):
        key = self.request.get('id')
        topic = self.M.Topics().find(key)

        comments = self.M.Comments().findall_by_topic(topic.key())

        self.tmpl.filename( 'topic/view.html' )
        self.tmpl.set(
            topic=topic,
            comments=comments
        )
        self.tmpl.render()

class add(CBase):
    def        post(self): self._post()
    def mobile_post(self): self._post()
    def       _post(self):
        topic = self.M.Topics()

        if self.users.get_current_user():
            topic.user = self.users.get_current_user()

        topic.title = self.request.get('title')
        topic.body  = self.request.get('body')
        topic.put()
        self.handler.redirect('/')
