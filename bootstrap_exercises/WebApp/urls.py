from django.urls import path
from django.conf.urls import url

from .views import Index, Note, AuthorView, TagView,\
    example, bootstrap_table, bootstrap, get_json,\
    NoteDetailView


urlpatterns = [
    path(r'', Index.as_view(), name='index'),
    path(r'note/', Note.as_view(), name='note'),
    url(r'^author/(?P<owner_id>\d+)/$', AuthorView.as_view(), name='author'),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag'),
    url(r'^post/(?P<post_id>\d+)$', NoteDetailView.as_view(), name='noteDetail'),
    path(r'example/', example, name='example'),
    path(r'boot/', bootstrap, name='bootstrap'),
    path(r'table/', bootstrap_table, name='bootstrap_table'),
    url(r'^table_data', get_json, name='table_data'),
]
