from django.shortcuts import render
from .models import Student


def index(request):
    # v1: 实现传递一个单词到index页面进行渲染
    # words = 'World!'
    # return render(request, 'index.html', context={'words': words, 'student_name': 'Eric'})

    # v2: 实现传递一个对象列表到index页面进行渲染
    students = Student.objects.all()
    return render(request, 'index.html', context={'students': students})
