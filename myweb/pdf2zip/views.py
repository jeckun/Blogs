from django.shortcuts import render
from django.http import FileResponse, HttpResponse, HttpResponseRedirect
from django.utils.http import urlquote
from django.urls import reverse
from django.views import View

import os

from .models import Compression_log
from .lib.pdf2png import Pdf

context = {
    'title': 'Pdf2zip | We provide PDF compression services',
    'name': 'Pdf2zip',
    'inf': 'Copy right by Eric.',
    'ip': '',
    'filelist': [],
    'state': 0,
    'error': 0,
}


def get_filelist(path):
    context['filelist'].clear()
    for cur, dir, files in os.walk(path):
        for f in files:
            context['filelist'].append(f)
    if len(context['filelist']) == 0:
        context['state'] = 0
    else:
        context['state'] = 1
    print('filelist is %s' % context['filelist'])


class index(View):
    template_name = 'index.html'
    cmp = Compression_log()
    context = context

    def get(self, request):
        self.context['ip'] = request.META['REMOTE_ADDR']
        path = os.path.join("./pdf2zip/upload/" + self.context['ip'])
        get_filelist(path)
        # self.context['inf'] = 'Copy right by Eric.'
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
            get_filelist(path)

            return HttpResponseRedirect(reverse('index'))


def compression(request):
    # 压缩选定的文件
    if request.method == "POST":
        context['ip'] = request.META['REMOTE_ADDR']
        filename = request.POST['filename']
        path = os.path.join("./pdf2zip/upload/" + context['ip'])
        file = os.path.join(path, filename)

        if 'compress' in request.POST:
            # 压缩Pdf文件
            context['inf'] = '开始压缩%s.' % filename
            compress = 0.8
            pdf = Pdf(file)
            pdf.from_png(pdf.to_png(compress=compress))
            context['inf'] = '压缩%s完成.' % filename
            print('compress %s' % file)
        elif 'delete' in request.POST:
            print('delete %s' % filename)
            # 删除Pdf文件
            os.remove(file)
            context['inf'] = '%s已经被删除！' % filename
            print('delete %s' % file)
        elif 'download' in request.POST:
            print('download %s' % filename)
            context['inf'] = '开始下载%s！' % filename
            file=open(file, 'rb')
            response = FileResponse(file)
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename={0}'.format(urlquote(filename))
            return response

        else:
            pass

        print('get_filelist %s' % path)
        get_filelist(path)

        return HttpResponseRedirect(reverse('index'))

