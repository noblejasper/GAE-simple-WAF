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

