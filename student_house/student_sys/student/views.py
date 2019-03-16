from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import StudentForm
from .models import Student


def index(request):
    # v1: 实现传递一个单词到index页面进行渲染
    # words = 'World!'
    # return render(request, 'index.html', context={'words': words, 'student_name': 'Eric'})

    # v2: 实现传递一个对象列表到index页面进行渲染
    # students = Student.objects.all()
    # return render(request, 'index.html', context={'students': students})

    # v3: 最终效果
    # students = Student.objects.all()
    students = Student.get_all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # cleaned_data：清洗数据。
            # 该对象用于将Form上字段的数据按字段类型进行转换
            # 会调用我们在forms中定义的cleaned函数
            # cleaned_data = form.cleaned_data
            # student = Student()
            # student.name = cleaned_data['name']
            # student.sex = cleaned_data['sex']
            # student.email = cleaned_data['email']
            # student.profession = cleaned_data['profession']
            # student.qq = cleaned_data['qq']
            # student.phone = cleaned_data['phone']
            # student.save()
            # return HttpResponseRedirect(reverse('index'))

            # 上面使用手工方法来保存从表单上传递过来的数据
            # 其实在ModelForm中已经有这个方法，可以简化为下面这句
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = StudentForm()

    context = {
        'students': students,
        'form': form,
    }
    return render(request, 'index.html', context=context)
