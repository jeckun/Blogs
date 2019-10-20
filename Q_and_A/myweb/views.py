from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User

from myweb.models import Questions, Answer
from myweb.forms import QuestionsForm, AnswerForm


def get_user(request):
    """
    判断用户是否登录，登录成功返回的是用户对象，否则返回访问者。
    """
    user = request.user
    if isinstance(user, User):
    # if request.user.is_authenticated():
        return user
    else:
        return get_object_or_404(User, username='visitor')


class question(ListView):
    model = Questions
    paginate_by = 5
    context_object_name = 'questions'
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        # user = get_user(request)
        context = self.get_context_data(**kwargs)
        # context.update({'user': {'id': user.id, 'name': user.username, }})
        context.update({'question_number': self.get_queryset().count()})
        return render(request, 'index.html', context=context)

    def get_context_data(self, **kwargs):
        """ 传递问题表单进行渲染 """
        context = super().get_context_data(**kwargs)
        context.update({'questions_form': QuestionsForm})
        context.update({'answer_form': AnswerForm})
        return context

    def get_queryset(self):
        """ 按时间倒序 """
        queryset = super().get_queryset()
        return queryset.order_by('-datetime')

    def post(self, request):
        form = QuestionsForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            qst = Questions()
            qst.title = cleaned_data['title']
            qst.content = cleaned_data['content']
            qst.owner = get_user(request)
            qst.save()
        return HttpResponseRedirect(reverse('index'))


def answer(request):
    form = AnswerForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        ans = Answer()
        ans.content = cleaned_data['content']
        ans.owner = get_user(request)
        ans.question = cleaned_data['question']
        ans.save()
        print(get_user(request))
        print('saved')
    else:
        print('is not valid.')
    return HttpResponseRedirect(reverse('index'))


def thumbs(request, pk):
    qst = get_object_or_404(Questions, id=pk)
    qst.thumbs_up += 1
    qst.save()
    return HttpResponseRedirect(reverse('index'))


def test(request):
    return render(request, 'test.html')


class SearchView(ListView):
    def get_context_data(self):
        keyword = self.request.GET.get('keyword')
        context = super().get_queryset()
        context.update({'keyword': keyword })
        return context

    def get_queryset(self):
        return super().get_queryset()
