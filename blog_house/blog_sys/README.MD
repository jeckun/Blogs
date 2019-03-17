# 博客系统

这个博客系统是用 Django2.1.7+python3.7 搭建的。下面是搭建过程以及关键代码。

## 环境检查

```buildoutcfg
$ python --version
Python 3.7.2
$ python -m django --version
2.1.7
```

如果不是上述环境，可以对应安装

```buildoutcfg
$ pip3 install django
```

## 创建站点

```buildoutcfg
$ mkdir blog_house
$ cd blog_house && django-admin startproject blog_sys
$ cd blog_house/blog_sys
$ python manage.py startapp blog
```

## 添加应用，并进行基础设置

打开settings.py，在修改如下位置。

```buildoutcfg
# 添加应用
INSTALLED_APPS = [
    'blog',
    ......
]

# 设置语言
LANGUAGE_CODE = 'zh-hans'

# 设置时区
TIME_ZONE = 'Asia/shanghai'
```

## 创建模型

这里创建博客所有需要存储的对象，例如：

-用户端：文章、分类、标签、友链、评论等
-管理端：用户

首先打开blog目录下的models，添加如下代码

```buildoutcfg
class blog(model.Model):
```

## 创建后台

因为Django自带后台管理工具，可以使用Django自带后台。

```buildoutcfg
$ python manage.py makemigrations
$ python manage.py migrate
# 创建用户
$ python manage.py createsuperuser
```
