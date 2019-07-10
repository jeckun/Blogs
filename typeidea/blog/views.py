from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Tag, Category, Link


def post_list(request, category_id=None, tag_id=None):
    """
    用于展示文章列表，返回一组文章的名称和摘要
    """
    category = None
    tag = None
    # post_list = Post.objects.filter(status=Post.STATUS_NORMAL)
    post_list = Post.latest_posts()

    # if tag_id:
    #     try:
    #         tag = Tag.objects.get(id=tag_id)
    #         # post_list = tag.post_set.filter(status=Post.STATUS_NORMAL)
    #         post_list = tag.post_set.all()
    #     except Tag.DoesNotExist:
    #         post_list = []
    #
    # if category_id:
    #     try:
    #         category = Category.objects.get(id=category_id)
    #         post_list = post_list.filter(category_id=category_id)
    #     except Post.DoesNotExist:
    #         post_list = []

    if tag_id:
        post_list, tag = Post.get_by_tag(tag_id)

    if category_id:
        post_list, category = Post.get_by_category(category_id)

    context={
        'category': category,
        'tag': tag,
        'post_list': post_list,
    }
    context.update(Category.get_navs())

    return render(request, 'blog/list.html', context=context)


# def post_detail(request, post_id):
#     # 测试验证URL是否正确
#     return HttpResponse('detail')
def post_detail(request, post_id):
    """
    显示文章内容明细
    """
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None
    context = { 'post': post, }
    context.update(Category.get_navs())
    return render(request, 'blog/detail.html', context=context)


def links(request):
    # 测试验证URL是否正确
    # return HttpResponse('links')
    return render(request, 'blog/links.html', context={'name': 'links'})
