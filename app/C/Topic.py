from nobjas.C import CBase

class view(CBase):
    def get(self):
        key = self.request.get('id')
        topic = self.M.Topics().find(key)

        comments = self.M.Comments().findall_by_topic(topic.key())

        template = self.tmpl( self, 'topic/view.html' )
        template.set(
            topic=topic,
            comments=comments
        )
        template.render()

class add(CBase):
    def post(self):
        topic = self.M.Topics()

        if self.users.get_current_user():
            topic.user = self.users.get_current_user()

        topic.title = self.request.get('title')
        topic.body  = self.request.get('body')
        topic.put()
        self.handler.redirect('/')
