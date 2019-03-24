from django.db import models

"""
服务报告：

记录每次服务的对象以及服务的结果，并进行分析后进行反馈。

"""


class Compression_log(models.Model):
    __name__ = '压缩日志'

    STEP_ITEMS = [
        (0, '请上传待压缩的PDF文件'),
        (1, '上传成功，待压缩'),
        (2, '压缩成功，待下载'),
        (3, '下载成功，完成！'),
    ]

    ip = models.CharField(max_length=100, verbose_name='ip地址')
    filename = models.CharField(max_length=100, verbose_name='源文件名', blank=True, null=True)
    state = models.IntegerField(verbose_name='状态', choices=STEP_ITEMS, default=0)
    before_size = models.FloatField(verbose_name='压缩前大小', max_length=10, blank=True, null=True)
    after_size = models.FloatField(verbose_name='压缩后大小', max_length=10, blank=True, null=True)
    compression_ratio = models.FloatField(verbose_name='压缩比', max_length=10, blank=True, null=True)
    datetime = models.DateTimeField(verbose_name='日期', auto_now_add=True)

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = verbose_name_plural = '压缩日志'
