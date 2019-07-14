from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView
from blog.models  import Post


class Content:
    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs)
        content.update({
            'nav': '首页',
        })
        content.update({
            'foot': '页脚'
        })
        return content


# Create your views here.
class PostViews(Content, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'index.html'
