from django.shortcuts import render
from django.http import HttpResponse


def post_list(request, category_id=None, tag_id=None):
    return render(request, 'blog/list.html', context={'name': 'post_list'})


# def post_detail(request, post_id):
#     # 测试验证URL是否正确
#     return HttpResponse('detail')

def post_detail(request, post_id):
    return render(request, 'blog/detail.html', context={'name': 'post_detail'})


def links(request):
    # 测试验证URL是否正确
    # return HttpResponse('links')
    return render(request, 'blog/links.html', context={'name': 'links'})