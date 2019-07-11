from django.db import models
from django.contrib.auth.models import User
from django.template.loader import render_to_string


class Tag(models.Model):
    # 标签
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    name = models.CharField(max_length=10, verbose_name='名称')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='状态')
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.SET_NULL, blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.name

    # 侧边栏
    @classmethod
    def get_all(cls):
        return cls.objects.filter(status=Tag.STATUS_NORMAL)

    class Meta:
        verbose_name = verbose_name_plural = '标签'


class Category(models.Model):
    # 分类
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    name = models.CharField(max_length=50, verbose_name='名称')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='状态')
    is_nav = models.BooleanField(default=False, verbose_name='是否为导航')
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.SET_NULL, blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.name

    @classmethod
    def get_navs(cls):
        # 获取分类列表和标记为导航的分类列表
        categories = cls.objects.filter(status=Category.STATUS_NORMAL)
        nav_categories = []
        normal_categories = []
        for cate in categories:
            if cate.is_nav:
                nav_categories.append(cate)
            else:
                normal_categories.append(cate)
        return { 'navs': nav_categories, 'categories': normal_categories, }

    class Meta:
        verbose_name = verbose_name_plural = '分类'


class Post(models.Model):
    # 文章
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
        (STATUS_DRAFT, '草稿')
    )

    title = models.CharField(max_length=255, verbose_name='标题')
    desc = models.CharField(max_length=1024, blank=True, verbose_name='摘要')
    content = models.TextField(verbose_name='正文', help_text='正文必须为MarkDown格式')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='状态')
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.SET_NULL, blank=True, null=True)
    tag = models.ManyToManyField(Tag, verbose_name='标签')
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.SET_NULL, blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    pv = models.PositiveIntegerField(default=1)   # 浏览量点击量
    uv = models.PositiveIntegerField(default=1)   # 独立访客

    def __str__(self):
        return self.title

    @staticmethod
    def get_by_tag(tag_id):
        # 根据标签获取文章列表
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            tag = None
            post_list = []
        else:
            post_list = tag.post_set.filter(status=Post.STATUS_NORMAL).select_related('owner', 'category')
        return post_list, tag

    @staticmethod
    def get_by_category(category_id):
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            category=None
            post_list = []
        else:
            post_list = category.post_set.filter(status=Post.STATUS_NORMAL).select_related('owner', 'category')
        return post_list, category

    @classmethod
    def latest_posts(cls):
        queryset = cls.objects.filter(status=cls.STATUS_NORMAL)
        return queryset

    @classmethod
    def hot_posts(cls):
        return cls.objects.filter(status=cls.STATUS_NORMAL).order_by('-pv')

    class Meta:
        verbose_name = verbose_name_plural = '文章'
        ordering = ['-id']    # 根据id降序排列


class Comment(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    target = models.ForeignKey(Post, verbose_name='评论目标', on_delete=models.SET_NULL, blank=True, null=True)
    content = models.CharField(max_length=2000, verbose_name='内容')
    nickname = models.CharField(max_length=50, verbose_name='昵称')
    website = models.URLField(verbose_name='网站')
    email = models.EmailField(verbose_name='邮箱')
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.SET_NULL, blank=True, null=True)
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='状态')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = verbose_name_plural = '评论'

class Link(models.Model):
    # 友链
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    title = models.CharField(max_length=50, verbose_name='标题')
    href = models.URLField(verbose_name='链接')
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='状态')
    weight = models.PositiveIntegerField(default=1, choices=zip(range(1, 6), range(1, 6)),
                                         verbose_name='权重', help_text='权重高排名靠前')
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.SET_NULL, blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = '友链'


class SideBar(models.Model):
    """侧边栏"""
    STATUS_SHOW = 0
    STATUS_HIDE = 1
    STATUS_ITEM = (
        (STATUS_SHOW, '显示'),
        (STATUS_HIDE, '隐藏'),
    )

    DISPLAY_HTML = 1
    DISPLAY_LATEST = 2
    DISPLAY_HOT = 3
    DISPLAY_COMMENT = 4
    SIDE_TYPE = (
        (DISPLAY_HTML, 'HTML'),
        (DISPLAY_LATEST, '最新文章'),
        (DISPLAY_HOT, '最热文章'),
        (DISPLAY_COMMENT, '最近评论'),
    )

    """字段"""
    title = models.CharField(max_length=50, verbose_name='标题')
    display_type = models.PositiveIntegerField(verbose_name='显示类型', default=1, choices=SIDE_TYPE)
    content = models.CharField(max_length=500, blank=True, verbose_name='内容', help_text='如果设置的不是HTML类型，可为空')
    status = models.PositiveIntegerField(default=STATUS_SHOW, choices=STATUS_ITEM, verbose_name='状态')
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.SET_NULL, blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '侧边栏'

    def __str__(self):
        return self.title

    @classmethod
    def get_all(cls):
        return cls.objects.filter(status=cls.STATUS_SHOW)

    @property
    def content_html(self):
        """直接渲染模板"""

        result = ''
        if self.display_type == self.DISPLAY_HTML:
            result = self.content
        elif self.display_type == self.DISPLAY_LATEST:
            context = {'posts': Post.latest_posts()}
            result = render_to_string('blocks/sidebar_posts.html', context)
        elif self.display_type == self.DISPLAY_HOT:
            context = {'posts': Post.hot_posts()}
            result = render_to_string('blocks/sidebar_posts.html', context)
        elif self.display_type == self.DISPLAY_COMMENT:
            context = {
                'comments': Comment.objects.filter(status=Comment.STATUS_NORMAL)
            }
            result = render_to_string('blocks/sidebar_comments.html', context)

        return result
