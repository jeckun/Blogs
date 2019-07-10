博客网址搭建过程：

1、创建项目和应用

$ django-admin startproject typeidea
$ cd typeidea
$ django-admin startapp blog


2、进行基础配置

typeidea/settings.py

修改：
1）INSTALLED_APPS 添加'blog'
2）LANGUAGE_CODE = 'zh-hans'
3）TIME_ZONE = 'Asia/Shanghai'


3、创建数据结构

blog/models.py

添加：
文章Post、标签Tag、分类Category、友链Link的数据结构


4、创建后台

blog/admin.py

1）首先引用Models
from .models import Post, Tag, Category, Link

2）创建基类
为了实现每个用户只能查看本人创建的内容，抽象基类BaseOwnerAdmin实现对象保存时记录操作人员。以及浏览时只能看到自己创建的对象。

3）创建各个对象管理类
每个对象都从基类派生。如：class TagAdmin(BaseOwnerAdmin)

4）注册管理后台对象
@admin.register(Tag)

至此后台创建完毕，开始创建前台。


5、展示博客
1) 规划URL
首页： 127.0.0.1/
博文详情页： 127.0.0.1/post/<post_id>.html
分类列表页： 127.0.0.1/category/<category_id>
标签列表页： 127.0.0.1/tag/<tag_id>
友链列表页： 127.0.0.1/link/<link_id>

2) 创建View函数
blog.views
return render(request, 'blog/detail.html', context={'name': 'post_list'})

3) 挂接模板

3) 修改URL路由

