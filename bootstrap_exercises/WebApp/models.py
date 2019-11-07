from django.db import models
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField

import datetime


class Tag(models.Model):
    """ 标签 """
    tag = models.CharField(max_length=100, verbose_name='标签')
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = verbose_name_plural = '标签'


class Post(models.Model):
    """ 文章标题和内容 """
    title = models.CharField(max_length=100, verbose_name='标题')
    content = models.TextField(verbose_name='摘要')
    ueditorcontent = UEditorField(width=1200, height=300, toolbars="full", imagePath="images/", filePath="files/", upload_settings={"imageMaxSize": 1204000}, settings={}, verbose_name='正文', default=None, null=True, blank=True)
    tag = models.ManyToManyField(Tag, verbose_name='标签')
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.SET_NULL, blank=True, null=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    def __str__(self):
        return self.title

    def get_active_user(self):
        user = self.objects.filter(create_time__gt=datetime.date(2019, 11, 1))\
            .distinct().values('owner')            # gt 表示大于等于
        return User.objects.filter(pk__in=user)    # pk in user 这里user是一个列表

    def get_tags(self):
        return Tag.objects.filter(pk__in=self.tag).values('tag')

    def archive(self):
        """ 归档年月 """
        return self.create_time.strftime('%Y-%m')
        archive.short_description = '归档年月'

    class Meta:
        verbose_name = verbose_name_plural = '文章'