# -*- coding: utf-8 -*-
from google.appengine.ext import db

class Tasks(db.Model):
    creater  = db.UserProperty('作成者', auto_current_user=False, auto_current_user_add=True)
    owner    = db.UserProperty('オーナー', auto_current_user=False, auto_current_user_add=False )
    changer  = db.UserProperty('変更者', auto_current_user=False, auto_current_user_add=True )
    title    = db.StringProperty('タスク名')
    body     = db.TextProperty('タスク詳細')
    category = db.ReferenceProperty(Categories, verbose_name='カテゴリー')
    parent   = db.SelfReferencePropert('親タスク')
    status   = db.TextProperty('ステータス', default="normal")
    created  = db.DateTimeProperty('作成日', auto_now_add=True)
    modified = db.DateTimeProperty('変更日', auto_now=True)

    per_page = 20

    def paginate(self, page=1, status='normal'):
        limit    = self.per_page
        offset   = self.per_page * (page -1)
        q = db.GqlQuery("SELECT * FROM Tasks WHERE status = :status ORDER BY created DESC", status=status)
        return q.fetch(limit, offset)

    def findall_by_parent(self, key, status='normal'):
        q = db.GqlQuery("SELECT * FROM Tasks WHERE status = :status AND parent = :parent ORDER BY created DESC", status=status, parent=key)
        return q.fetch(self.per_page)

    def findall_by_owner(self, user, status='normal'):
        q = db.GqlQuery("SELECT * FROM Tasks WHERE status = :status AND owner = :user ORDER BY created DESC", status=status, user=user)
        return q.fetch(self.per_page)

    def findall_by_category(self, category, status='normal'):
        q = db.GqlQuery("SELECT * FROM Tasks WHERE status = :status AND category = :category ORDER BY created DESC", status=status, category=category)
        return q.fetch(self.per_page)

class Categories(db.Model):
    title       = db.StringProperty('カテゴリー名')
    description = db.TextProperty('カテゴリー説明')
    status      = db.TextProperty('ステータス', default="normal")
    created     = db.DateTimeProperty('作成日', auto_now_add=True)
    modified    = db.DateTimeProperty('変更日', auto_now=True)

class Topics(db.Model):
    user     = db.UserProperty()
    title    = db.StringProperty()
    body     = db.TextProperty()
    status   = db.IntegerProperty(default=0)
    created  = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now=True)

    def findall(self):
        q = db.GqlQuery("SELECT * FROM Topics WHERE status = :1 ORDER BY created DESC", 0)
        return q.fetch(10)

    def find(self, key):
        return db.get(key)

class Comments(db.Model):
    topic    = db.ReferenceProperty(Topics)
    user     = db.UserProperty()
    body     = db.TextProperty()
    status   = db.IntegerProperty(default=0)
    created  = db.DateTimeProperty(auto_now_add=True)
    modified = db.DateTimeProperty(auto_now=True)

    def findall_by_topic(self, key):
        q = db.GqlQuery("SELECT * FROM Comments WHERE topic = :1 AND status = :2 ORDER BY created DESC", key, 0)
        return q.fetch(10)
