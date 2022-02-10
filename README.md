# myBlog
博客的首页截图
![image](https://github.com/EdwardLiu-Aurora/myBlog/blob/master/index.png)
#static存放着所有前端内容
# 第一步，进行数据库配置
在Online-->settings.py中对DATABASES进行配置
'default': {
        'ENGINE': 'django.db.backends.mysql',   # 数据库引擎
        'NAME': 'DjBlog',                       # 数据库名称
        'USER': 'root',                      # 数据库登录用户名
        'HOST': '127.0.0.1',                # 数据库主机IP，如保持默认，则为127.0.0.1
        'PORT': 3307,                           # 数据库端口号，如保持默认，则为3306

    }
