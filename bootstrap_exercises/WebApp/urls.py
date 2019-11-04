
from django.urls import path
from django.conf.urls import url

from .views import index, note, example, bootstrap_table, bootstrap, get_json


urlpatterns = [
    path(r'', index, name='index'),
    path(r'note/', note, name='note'),
    path(r'example/', example, name='example'),
    path(r'boot/', bootstrap, name='bootstrap'),
    path(r'table/', bootstrap_table, name='bootstrap_table'),
    url(r'^table_data', get_json, name='table_data'),
]
