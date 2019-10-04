from datetime import date

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView
from django.shortcuts import get_object_or_404
from django.db.models import Q, F
from django.core.cache import cache

from .models import Post, Tag, Category, Link, SideBar, Comment
from .forms import CommentForm


class CommonViewMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            # 返回所有侧边栏对象
            'sidebars': SideBar.get_all(),
            # 返回评论模板对象
            'comment_form': CommentForm,
            # 返回评论列表
            # 'comment_list': Comment.get_by_target(self.request.path),
            'comment_list': Comment.get_by_target(self.kwargs.get('post_id')),
        })
        context.update(Category.get_navs())
        return context


class PostListView(CommonViewMixin, ListView):
    """ 博客列表页 """
    queryset = Post.get_all()
    paginate_by = 8                     # 文章列表分页展示数量
    context_object_name = 'post_list'   # 此处定义模版中使用的变量名，如果不定义，默认是object_list
    template_name = 'blog/clslist.html'


class PostDetailView(CommonViewMixin, DetailView):
    """ 博客详情页类实现 """
    # model = Post
    queryset = Post.get_all()
    template_name = 'blog/clsDetail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'    # 如果不定义这个，默认变量为pk

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        self.handle_visited()
        return response

    def handle_visited(self):
        # 用来记录页面访问次数的
        increase_pv = False
        increase_uv = False
        uid = self.request.uid           # 由前端提供的用户唯一标识，这个标识在middleware.user_id中定义的
        pv_key = 'pv:%s:%s' % (uid, self.request.path)
        uv_key = 'uv:%s:%s:%s' % (uid, str(date.today()), self.request.path)

        if not cache.get(pv_key):
            increase_pv = True
            cache.set(pv_key, 1, 1*60)     # 1分钟有效

        if not cache.get(uv_key):
            increase_uv = True
            cache.set(pv_key, 1, 24*60*60)   # 24小时有效

        if increase_pv and increase_uv:
            Post.objects.filter(pk=self.object.id).update(pv=F('pv') + 1, uv=F('uv') + 1)
        elif increase_pv:
            Post.objects.filter(pk=self.object.id).update(pv=F('pv') + 1)
        elif increase_uv:
            Post.objects.filter(pk=self.object.id).update(uv=F('uv') + 1)



class CommentView(TemplateView):
    # 评论
    http_method_names = ['post']
    template_name = 'blog/result.html'

    def post(self, request, *args, **kwargs):
        # 获取请求中的表单对象
        comment_form = CommentForm(request.POST)
        # 从请求字符串中获取参数
        target = request.POST.get('target')
        post_id = request.POST.get('post_id')
        # 判断表单校验是否正确
        if comment_form.is_valid():
            # 获取评论表单对象实例
            instance = comment_form.save(commit=False)
            # 给评论加上与文章的关联，需要返回的是Post对象
            instance.target = get_object_or_404(Post, pk=post_id)
            # instance.target = Post.get_by_id(post_id)[0]
            instance.save()
            succeed = True
            return redirect(target)     # 提交成功之后在跳转回原来的页面，这里target就是要跳回的页面路径
        else:
            succeed = False

        # 提交失败后，将失败信息传递到前端，然后显示默认模板
        context = {
            'succeed': succeed,
            'form': comment_form,
            'target': target,
        }
        return self.render_to_response(context=context)


class CategoryView(PostListView):
    def get_context_data(self, **kwargs):
        """ 重写context_date，向模版数据添加分类数据 """
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        category = get_object_or_404(Category, pk=category_id)
        context.update({
            'category': category
        })
        return context

    def get_queryset(self):
        """ 重写queryset，根据分类过滤 """
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id)


class TagView(PostListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag_id')
        tag = get_object_or_404(Tag, pk=tag_id)
        context.update({
            'tag': tag
        })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        tag_id = self.kwargs.get('tag_id')
        return queryset.filter(id=tag_id)


# 查询视图实现
class SearchView(PostListView):
    def get_context_data(self):
        context = super().get_context_data()
        context.update(
            {'keyword': self.request.GET.get('keyword', '')}
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.request.GET.get('keyword')
        if not keyword:
            return queryset
        return queryset.filter(Q(title__icontains=keyword) | Q(desc__icontains=keyword))


# 作者视图，实现按作者过滤
class AuthorView(PostListView):
    def get_queryset(self):
        queryset = super().get_queryset()
        author_id = self.kwargs.get('owner_id')
        return queryset.filter(owner_id=author_id)


def links(request):
    # 测试验证URL是否正确
    # return HttpResponse('links')
    return render(request, 'blog/links.html', context={'name': 'links'})


# 显示交换链接
class LinkListView(CommonViewMixin, ListView):
    queryset = Link.objects.filter(status=Link.STATUS_NORMAL)
    template_name = 'config/links.html'
    context_object_name = 'link_list'


# def post_list(request, category_id=None, tag_id=None):
#     """
#     用于展示文章列表，返回一组文章的名称和摘要
#     """
#     category = None
#     tag = None
#     # post_list = Post.objects.filter(status=Post.STATUS_NORMAL)
#     post_list = Post.latest_posts()
#
#     # if tag_id:
#     #     try:
#     #         tag = Tag.objects.get(id=tag_id)
#     #         # post_list = tag.post_set.filter(status=Post.STATUS_NORMAL)
#     #         post_list = tag.post_set.all()
#     #     except Tag.DoesNotExist:
#     #         post_list = []
#     #
#     # if category_id:
#     #     try:
#     #         category = Category.objects.get(id=category_id)
#     #         post_list = post_list.filter(category_id=category_id)
#     #     except Post.DoesNotExist:
#     #         post_list = []
#
#     # 将post_list以及category/tag的实现逻辑，拆分到Model中实现，简化代码
#     if tag_id:
#         post_list, tag = Post.get_by_tag(tag_id)
#
#     if category_id:
#         post_list, category = Post.get_by_category(category_id)
#
#     context={
#         'category': category,
#         'tag': tag,
#         'post_list': post_list,
#         'sidebars': SideBar.get_all(),
#     }
#     context.update(Category.get_navs())
#     # update 导致context中增加navs和categories
#
#     return render(request, 'blog/list.html', context=context)


# def post_detail(request, post_id):
#     # 测试验证URL是否正确
#     return HttpResponse('detail')

# def post_detail(request, post_id):
#     """
#     函数方式显示文章内容明细
#     """
#     try:
#         post = Post.objects.get(id=post_id)
#     except Post.DoesNotExist:
#         post = None
#     context = { 'post': post, }
#     context.update(Category.get_navs())
#     return render(request, 'blog/detail.html', context=context)
