from django.db import models
from django.contrib.auth.models import User


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
    content = models.TextField(verbose_name='正文')
    tag = models.ManyToManyField(Tag, verbose_name='标签')
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.SET_NULL, blank=True, null=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = verbose_name_plural = '文章'