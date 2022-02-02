import pandas
import pymysql
from django.shortcuts import render
from pymysql import *
from django.views.generic import FormView
import pandas as pd
# 数据库连接
class DBcon:
    """连接数据库"""
    def __init__(self):
        self.con = connect(host = '127.0.0.1',user = 'root',port = 3307,db = 'DjBlog',charset = 'utf8')
    def data_all(self):
        cur = self.con.cursor(pymysql.cursors.DictCursor)
        cur.execute("select * from article limit 10")
        return cur.fetchall()
    def data_id(self):
        cur = self.con.cursor(pymysql.cursors.DictCursor)
        cur.execute("select id from article limit 10")
        return cur.fetchall()

data = DBcon().data_all()

# 首页-页面
class FontPage(FormView):
    def get(self,request, *args, **kwargs):
        return render(request,'polls/index.html',{'data':data})
# 关于我-页面
class About(FormView):
    def get(self, request, *args, **kwargs):
        return render(request,'polls/about.html')

# 归档-页面
class Archives(FormView):
    def get(self, request, *args, **kwargs):
        return render(request,'polls/archives.html')

# 文章-页面
class Blog(FormView):
    def get(self, request, *args, **kwargs):

        return render(request,'polls/blog.html',{'data':data})
# 标签-页面
class Tags(FormView):
    def get(self, request, *args, **kwargs):
        return render(request,'polls/tags.html')
# 分类-页面
class Types(FormView):
    def get(self, request, *args, **kwargs):
        return render(request,'polls/types.html')


