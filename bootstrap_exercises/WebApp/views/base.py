from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User
from ..config import APP_INF
from ..models import Post


# def index(request, *args, **kwargs):
#     context = {}
#     update_app_inf_nav_menu_current('index')
#     context.update(APP_INF)
#     return render(request, "base/index.html", context)


class Index(ListView):
    model = Post
    paginate_by = 3
    context_object_name = 'Post'
    template_name = 'base/index.html'

    def get_context_data(self, **kwargs):
        """ 传递问题表单进行渲染 """
        context = super().get_context_data(**kwargs)
        update_app_inf_nav_menu_current('index')
        context.update(APP_INF)
        return context

    def get_queryset(self):
        """ 按时间倒序 """
        queryset = super().get_queryset()
        return queryset.order_by('-create_time')


# def note(request, *args, **kwargs):
#     context = {}
#     update_app_inf_nav_menu_current('note')
#     context.update(APP_INF)
#     return render(request, "base/note.html", context)


class Note(ListView):
    model = Post
    paginate_by = 5
    context_object_name = 'Post'
    template_name = 'base/note.html'

    def get_context_data(self, **kwargs):
        """ 传递问题表单进行渲染 """
        context = super().get_context_data(**kwargs)
        update_app_inf_nav_menu_current('note')
        context.update(APP_INF)
        return context

    def get_queryset(self):
        """ 按时间倒序 """
        queryset = super().get_queryset()
        return queryset.order_by('-create_time')


def example(request, *args, **kwargs):
    context = {}
    update_app_inf_nav_menu_current('example')
    context.update(APP_INF)
    return render(request, "base/example.html", context)


def update_app_inf_nav_menu_current(url_name):
    for item in APP_INF['NAV']['menu']:
        if APP_INF['NAV']['menu'][item]['url'] == url_name:
            APP_INF['NAV']['menu'][item]['current'] = True
        else:
            APP_INF['NAV']['menu'][item]['current'] = False
