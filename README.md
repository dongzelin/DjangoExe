# myBlog
博客的首页截图
![image](https://github.com/EdwardLiu-Aurora/myBlog/blob/master/index.png)
#static存放着所有前端内容
## 1.进行数据库配置

在Online-->settings.py中对DATABASES进行配置

```python
'default': {
'ENGINE': 'django.db.backends.mysql',   # 数据库引擎
'NAME': 'DjBlog',                       # 数据库名称
'USER': 'root',                      # 数据库登录用户名
'HOST': '127.0.0.1',                # 数据库主机IP，如保持默认，则为127.0.0.1
'PORT': 3307,                           # 数据库端口号，如保持默认，则为3306
}
```

## 2.配置ORM数据库

```python
#在与 settings.py 同级目录下的 init.py 中引入模块和进行配置
import pymysql
pymysql.install_as_MySQLdb()
```

在polls-->models.py 中进行编辑数据库

```python
from django.db import models	#导入models
class Blog(models.Model):
    id = models.AutoField(primary_key = True)   # 文章id
    title = models.CharField(max_length=60) # 标题
    runoob = models.TextField() # 文章内容
    runoob_author = models.CharField(max_length=60) # 作者
    submission_date = models.DateField()    # 时间
    type_name = models.CharField(max_length=60,default='') # 标签
```

之后运行以下代码

```python
$ python3 manage.py migrate   # 创建表结构
$ python3 manage.py makemigrations polls  # 让 Django 知道我们在我们的模型有一些变更
$ python3 manage.py migrate polls   # 创建表结构
```

3.启动本地文件

```python
$ python3 manage.py runserver 
```

启动文件进行访问
