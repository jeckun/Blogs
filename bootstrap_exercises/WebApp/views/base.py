import datetime
from dateutil.relativedelta import relativedelta

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User

from ..config import APP_INF
from ..models import Post, Tag


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


class Note(ListView):
    """ 博客列表页面 """
    model = Post
    paginate_by = 5
    context_object_name = 'Post'
    template_name = 'base/note.html'
    readonly_fields = ('archive',)

    def get_context_data(self, **kwargs):
        """ 传递问题表单进行渲染 """
        context = super().get_context_data(**kwargs)
        context.update({
            'Users': Post.get_active_user(Post),
        })
        context.update({
            'Tags': Tag.objects.all(),
        })
        context.update({
            'Months': archive_month(),
        })
        context.update({
            'Post_like_list': Post.order(Post, '-likes', 3),
        })
        update_app_inf_nav_menu_current('note')
        context.update(APP_INF)
        return context

    def get_queryset(self):
        """ 按时间倒序 """
        queryset = super().get_queryset()
        return queryset.order_by('-create_time')


class AuthorView(Note):
    """ 按用户过滤 """
    def get_queryset(self):
        queryset = super().get_queryset()
        author_id = self.kwargs.get('owner_id')
        return queryset.filter(owner_id=author_id)  # owner为一对多关系


class TagView(Note):
    """ 按Tag过滤 """
    def get_queryset(self):
        queryset = super().get_queryset()
        tag_id = self.kwargs.get('tag_id')
        return queryset.filter(tag=tag_id)  # tag为多对多关系


class NoteDetailView(DetailView):
    """ 博客详情页类实现 """
    model = Post
    # queryset = Post.objects.all()
    template_name = 'base/noteDetail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'    # 如果不定义这个，默认变量为pk

    def get_context_data(self, **kwargs):
        """ 传递问题表单进行渲染 """
        context = super().get_context_data(**kwargs)
        update_app_inf_nav_menu_current('note')
        context.update(APP_INF)
        return context

    # def get(self, request, *args, **kwargs):
    #     response = super().get(request, *args, **kwargs)
    #     self.handle_visited()
    #     return response

    # def handle_visited(self):
    #     # 用来记录页面访问次数的
    #     increase_pv = False
    #     increase_uv = False
    #     uid = self.request.uid           # 由前端提供的用户唯一标识，这个标识在middleware.user_id中定义的
    #     pv_key = 'pv:%s:%s' % (uid, self.request.path)
    #     uv_key = 'uv:%s:%s:%s' % (uid, str(date.today()), self.request.path)
    #
    #     if not cache.get(pv_key):
    #         increase_pv = True
    #         cache.set(pv_key, 1, 1*60)     # 1分钟有效
    #
    #     if not cache.get(uv_key):
    #         increase_uv = True
    #         cache.set(pv_key, 1, 24*60*60)   # 24小时有效
    #
    #     if increase_pv and increase_uv:
    #         Post.objects.filter(pk=self.object.id).update(pv=F('pv') + 1, uv=F('uv') + 1)
    #     elif increase_pv:
    #         Post.objects.filter(pk=self.object.id).update(pv=F('pv') + 1)
    #     elif increase_uv:
    #         Post.objects.filter(pk=self.object.id).update(uv=F('uv') + 1)


def example(request, *args, **kwargs):
    context = {}
    update_app_inf_nav_menu_current('example')
    context.update(APP_INF)
    return render(request, "base/example.html", context)


def update_app_inf_nav_menu_current(url_name):
    """ 更新顶部菜单活动状态 """
    for item in APP_INF['NAV']['menu']:
        if APP_INF['NAV']['menu'][item]['url'] == url_name:
            APP_INF['NAV']['menu'][item]['current'] = True
        else:
            APP_INF['NAV']['menu'][item]['current'] = False


def archive_month():
    """ 返回最近3个月字符串 """
    today = datetime.date.today()
    this_month = today.strftime("%Y-%m")
    last_1_month = today + datetime.timedelta(days=-today.day)
    last_2_month = today + relativedelta(months=-2)
    return [this_month, last_1_month.strftime("%Y-%m"), last_2_month.strftime("%Y-%m")]
