from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View

import os

from .models import Compression_log

context = {
    'title': 'Pdf2zip | We provide PDF compression services',
    'name': 'Pdf2zip',
    'message': '我们提供PDF压缩服务。',
    'inf': 'Copy right by Eric.',
    'ip': None,
    'upload': False
}

cmp = Compression_log()


def index(request):
    global context, cmp
    # if request.META.has_key('HTTP_X_FORWARDED_FOR'):
    #     ip = request.META['HTTP_X_FORWARDED_FOR']
    # else:
    #     ip = request.META['REMOTE_ADDR']
    ip = request.META['REMOTE_ADDR']
    context['ip'] = ip
    return render(request, "index.html", context=context)


def upload(request):
    global context
    if request.method == "POST":    # 请求方法为POST时，进行处理
        myFile = request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            context['inf'] = 'no files for upload!'
            context['upload'] = False
            return render(request, "index.html", context=context)
        destination = open(os.path.join("./pdf2zip/upload", myFile.name), 'wb+')    # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():      # 分块写入文件
            destination.write(chunk)
        destination.close()

        context['inf'] = ('上传%s成功！' % myFile.name)
        context['upload'] = True

        # return render(request, "index.html", context=context)
        return HttpResponseRedirect(reverse('index'))


def compression(request):
    context['inf'] = '压缩成功!'
    context['upload'] = False
    # return render(request, "index.html", context=context)
    return HttpResponseRedirect(reverse('index'))


def download(request):
    context['inf'] = '下载成功！'
    context['upload'] = False
    return HttpResponseRedirect(reverse('index'))
