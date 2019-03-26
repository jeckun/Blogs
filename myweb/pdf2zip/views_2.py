from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View

import os

from .models import Compression_log

context = {
    'title': 'Pdf2zip | We provide PDF compression services',
    'name': 'Pdf2zip',
    'inf': 'Copy right by Eric.',
    'ip': '',
    'filelist': [],
    'state': 0,
    'error': 0,
}


class index(View):
    template_name = 'index.html'
    cmp = Compression_log()
    context = context

    def get_filelist(self, path):
        self.context['filelist'].clear()
        for cur, dir, files in os.walk(path):
            for f in files:
                self.context['filelist'].append(f)

    def get(self, request):
        self.context['ip'] = request.META['REMOTE_ADDR']
        return render(request, self.template_name, context=self.context)

    def post(self, request):
        self.context['ip'] = request.META['REMOTE_ADDR']
        if request.method == "POST":  # 请求方法为POST时，进行处理
            myFile = request.FILES.get("file", None)  # 获取上传的文件，如果没有文件，则默认为None
            if not myFile:
                self.context['inf'] = '没有收到上传文件!'
                self.context['error'] = 1
                return render(request, self.template_name, context=self.context)

            name, exten = os.path.splitext(myFile.name)

            # 文件类型检查
            if exten.lower() != '.pdf':
                self.context['inf'] = '上传文件类型错误，请上传PDF格式文件!'
                self.context['error'] = 1
                return render(request, self.template_name, context=self.context)

            # 给每个用户一个独立的文件夹
            path = os.path.join("./pdf2zip/upload/" + self.context['ip'])
            if not os.path.isdir(path):
                os.mkdir(path)
            destination = open(os.path.join(path, myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
            for chunk in myFile.chunks():  # 分块写入文件
                destination.write(chunk)
            destination.close()

            # 返回消息
            self.context['inf'] = ('%s上传成功！' % myFile.name)
            self.context['state'] = 1
            self.context['error'] = 0
            self.get_filelist(path)

            return HttpResponseRedirect(reverse('index'))


def compression(request):
    if request.method == "POST":
        filename = request.POST['filename']
        context['inf'] = '开始压缩%s' % filename
        return HttpResponseRedirect(reverse('index'))
