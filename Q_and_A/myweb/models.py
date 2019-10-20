from django.db import models
from django.contrib.auth.models import User


# 提问
class Questions(models.Model):
    STATUS_NORMAL = 0
    STATUS_CLOSE = 1
    STATUS_ITEM = (
        (STATUS_NORMAL, "正常"),
        (STATUS_CLOSE, "关闭"),
    )

    title = models.CharField(max_length=100, verbose_name="问题")
    content = models.TextField(verbose_name="详细描述")
    datetime = models.DateTimeField(verbose_name="时间", auto_now_add=True)
    status = models.PositiveIntegerField(verbose_name="状态", default=STATUS_NORMAL, choices=STATUS_ITEM)
    owner = models.ForeignKey(User, verbose_name="提问者", on_delete=models.SET_NULL, blank=True, null=True)
    thumbs_up = models.IntegerField(verbose_name="点赞", default=0)
    comments = models.IntegerField(verbose_name="评论", default=0)

    def __str__(self):
        return self.title

    def get_all(self):
        return self.objects.all()

    class Meta:
        verbose_name = verbose_name_plural = "问题清单"


# 回答
class Answer(models.Model):
    owner = models.ForeignKey(User, verbose_name="响应者", on_delete=models.SET_NULL, null=True, blank=True)
    question = models.ForeignKey(Questions, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField(verbose_name="回答")
    datetime = models.DateTimeField(auto_now_add=True, verbose_name="时间")
    ip_address = models.CharField(max_length=10, verbose_name="IP地址")

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = verbose_name_plural = "回答列表"