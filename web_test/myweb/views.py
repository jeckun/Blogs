from django.shortcuts import render

context = {}


def index(request):
    context['message']='Hellow world.'
    return render(request, 'index.html', context=context)
