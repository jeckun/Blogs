from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Tag, Category, Link, SideBar
from django.views import View
from django.views.generic import DetailView, ListView
from django.shortcuts import get_object_or_404
from django.db.models import Q


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


class CommonViewMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'sidebars': SideBar.get_all(),
        })
        context.update(Category.get_navs())
        return context


# 查询视图实现
class SearchView(ListView):
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


class PostListView(CommonViewMixin, ListView):
    queryset = Post.latest_posts()
    paginate_by = 5                     # 文章列表分页展示数量
    context_object_name = 'post_list'   # 此处定义模版中使用的变量名，如果不定义，默认是object_list
    template_name = 'blog/clslist.html'


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

class PostDetailView(CommonViewMixin, DetailView):
    """ 博客详情页类实现 """
    # model = Post
    queryset = Post.latest_posts()
    template_name = 'blog/clsDetail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'    # 如果不定义这个，默认变量为pk


def links(request):
    # 测试验证URL是否正确
    # return HttpResponse('links')
    return render(request, 'blog/links.html', context={'name': 'links'})
