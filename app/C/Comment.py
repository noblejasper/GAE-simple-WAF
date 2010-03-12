# -*- coding: utf-8 -*-
from nobjas.C import CBase

class add(CBase):
    def get(self):
        topic_key = self.request.get('id')

        template = self.tmpl( self, 'comment/add.html' )
        template.set(
            topic_key=topic_key,
        )
        template.render()

    def post(self):
        comment = self.M.Comments()
        key     = self.request.get('id')

        topic = self.M.Topics().find(key)
        comment.topic = topic.key()
        comment.body  = self.request.get('body')

        if self.users.get_current_user():
            comment.user = self.users.get_current_user()

        comment.put()
        self.handler.redirect('/topic/view?id=' + key)

