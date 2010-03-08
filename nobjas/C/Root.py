from nobjas.C import CBase

class index(CBase):
    def get(self):
        topics       = self.M.Topics().findall()

        if self.users.get_current_user():
            auth_url          = self.users.create_logout_url(self.request.uri)
            auth_url_linktext = 'Logout'
        else:
            auth_url          = self.users.create_login_url(self.request.uri)
            auth_url_linktext = 'Login'

        template = self.tmpl( self, 'root/index.html' )
        template.set(
            topics=topics,
            auth_url=auth_url,
            auth_url_linktext=auth_url_linktext
        )
        template.render()

class guestbook(CBase):
    def post(self):
        topic = self.M.Topics()

        if self.users.get_current_user():
            topic.user = self.users.get_current_user()

        topic.title = self.request.get('title')
        topic.body  = self.request.get('body')
        topic.put()
        self.handler.redirect('/')

