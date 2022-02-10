from django.db import models


# Create your models here.
class Blog(models.Model):
    id = models.AutoField(primary_key = True)   # 文章id
    title = models.CharField(max_length=60) # 标题
    runoob = models.TextField() # 文章内容
    runoob_author = models.CharField(max_length=60) # 作者
    submission_date = models.DateField()    # 时间
    type_name = models.CharField(max_length=60,default='') # 标签
