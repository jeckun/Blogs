
from django.urls import path
from django.conf.urls import url

from .views import Index, Note, example, bootstrap_table, bootstrap, get_json


urlpatterns = [
    path(r'', Index.as_view(), name='index'),
    path(r'note/', Note.as_view(), name='note'),
    path(r'example/', example, name='example'),
    path(r'boot/', bootstrap, name='bootstrap'),
    path(r'table/', bootstrap_table, name='bootstrap_table'),
    url(r'^table_data', get_json, name='table_data'),
]
