
import pandas
import pymysql
from django.http import HttpResponse
from django.shortcuts import render
from pymysql import *
from django.views.generic import FormView
import pandas as pd
from django.forms.models import model_to_dict
from polls import models
from django.core.paginator import Paginator,Page,PageNotAnInteger
# 首页-页面
class FontPage(FormView):
    def get(self,request, *args, **kwargs):
        # 判断获取id
        if  request.GET.get('id'):
            # 获取前端id参数
            ids = request.GET.get('id')
            print('ttttttt', ids)
            # 根据前端id参数查询数据库数据，以字典形式呈现
            data_content = model_to_dict(models.Blog.objects.all(id = ids).first())
        # 判断获取标签名
        elif request.GET.get('type_name'):
            type_names = request.GET.get('type_name')
            # 根据前端id参数查询数据库数据
            data_content = models.Blog.objects.filter(type_name=type_names).values()
            # type_counts = models.Blog.objects.filter(type_name=type_names).count()
            type_countsXX = models.Blog.objects.filter(type_name='学习日志').count()
            type_countsSK = models.Blog.objects.filter(type_name='思考与感悟').count()
            type_countsQD = models.Blog.objects.filter(type_name='清单').count()
            type_countsJS = models.Blog.objects.filter(type_name='javaScript').count()
            type_countsCY = models.Blog.objects.filter(type_name='创业').count()
            type_countsSJ = models.Blog.objects.filter(type_name='认知升级').count()
            count_all = models.Blog.objects.filter(type_name=type_names).count()
        # 获取页面页数
        elif request.GET.get('page'):
            page_num = request.GET.get('page')
            print('页面数据',page_num)
            # 展示所有数据，一页展示5条
            datas_content = models.Blog.objects.all()
            paginator = Paginator(datas_content, 5)
            print('duanyan', len(datas_content), paginator.num_pages, paginator.count , paginator.validate_number(1))
            try:
                data_content = paginator.page(number=page_num)  # 这个num就是现实当前第几页
            except PageNotAnInteger:
                print('页码异常')
                data_content = paginator.page(number=1)
            # 统计所有数据个数
            count_all = models.Blog.objects.all().count()
            type_countsXX = models.Blog.objects.filter(type_name='学习日志').count()
            type_countsSK = models.Blog.objects.filter(type_name='思考与感悟').count()
            type_countsQD = models.Blog.objects.filter(type_name='清单').count()
            type_countsJS = models.Blog.objects.filter(type_name='javaScript').count()
            type_countsCY = models.Blog.objects.filter(type_name='创业').count()
            type_countsSJ = models.Blog.objects.filter(type_name='认知升级').count()
        # 如果都不是那么就展示首页数据信息
        else:
            print('首页')
            # 展示所有数据，一页展示5条
            data_content = models.Blog.objects.all().values()[:5]
            # 统计所有数据个数
            count_all = models.Blog.objects.all().count()
            type_countsXX = models.Blog.objects.filter(type_name='学习日志').count()
            type_countsSK = models.Blog.objects.filter(type_name='思考与感悟').count()
            type_countsQD = models.Blog.objects.filter(type_name='清单').count()
            type_countsJS = models.Blog.objects.filter(type_name='javaScript').count()
            type_countsCY = models.Blog.objects.filter(type_name='创业').count()
            type_countsSJ = models.Blog.objects.filter(type_name='认知升级').count()
        return render(request,'polls/index.html', {'data':data_content,
                                                   'data_count': count_all,
                                                   'type_countsXX':type_countsXX,
                                                   'type_countsSK':type_countsSK,
                                                   'type_countsQD':type_countsQD,
                                                   'type_countsJS':type_countsJS,
                                                   'type_countsCY':type_countsCY,
                                                   'type_countsSJ':type_countsSJ,
                                                               })

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
        # 获取前端id参数
        ids = request.GET.get('id')
        # 根据前端id参数查询数据库数据，以字典形式呈现
        data_content = model_to_dict(models.Blog.objects.filter(id=ids).first())
        return render(request,'polls/blog.html',{'data':data_content})

# 标签-页面
class Tags(FormView):
    def get(self, request, *args, **kwargs):
        return render(request,'polls/tags.html')
# 分类-页面
class Types(FormView):
    def get(self, request, *args, **kwargs):
        return render(request,'polls/types.html')


def polls_Blog(request):
    blog_connect = models.Blog(title = '测试文章1',runoob = '这是文章主题内容',runoob_author = '董泽林',submission_date = '2022-02-09')
    blog_connect.save()
    return HttpResponse('<p>数据添加成功!</p>')
