from django.apps import AppConfig


class MywebConfig(AppConfig):
    name = 'myweb'

    class Meta:
        verbose_name = verbose_name_plural = "提问"
