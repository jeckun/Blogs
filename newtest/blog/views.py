from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView
from blog.models  import Post


class Content:
    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs)
        content.update({
            'nav': '首页',
        })
        content.update({
            'foot': '页脚'
        })
        return content


# Create your views here.
class PostViews(Content, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'index.html'


def example(request, **kwargs):
    context = {
        'title': '洪虎的博客',
        'navs': ['技术', '生活'],
    }
    return render(request, "example.html", context=context)


def bootstrap(request, **kwargs):
    return render(request, "bootstrap.html", context=None)


def bootstrap_table(request, **kwargs):
    return render(request, "bootstrap_table.html", context=None)


def get_json(request, **kwargs):

    return


def dhr_index(request, **kwargs):
    return render(request, "dhr_index.html", context=None)


def dhr_org(request, **kwargs):
    return render(request, "dhr_organization_management.html", context=None)


def dhr_dept(request, **kwargs):
    return render(request, "dhr_department_management.html", context=None)


def dhr_dept_detail(request, **kwargs):
    return render(request, "dhr_department_detail.html", context=None)


def dhr_emp(request, **kwargs):
    return render(request, "dhr_employee_center.html", context=None)


def dhr_job_adj(request, **kwargs):
    return render(request, "dhr_job_adjustment.html", context=None)


def dhr_time(request, **kwargs):
    return render(request, "dhr_time_management.html", context=None)


def dhr_leave(request, **kwargs):
    return render(request, "dhr_leave_management.html", context=None)


def dhr_overtime(request, **kwargs):
    return render(request, "dhr_overtime_management.html", context=None)


def dhr_trip(request, **kwargs):
    return render(request, "dhr_trip_management.html", context=None)


def dhr_benefit(request, **kwargs):
    return render(request, "dhr_benefit_management.html", context=None)


def dhr_payroll(request, **kwargs):
    return render(request, "dhr_payroll_management.html", context=None)


def dhr_recruitment(request, **kwargs):
    return render(request, "dhr_recruitment_management.html", context=None)


def dhr_training(request, **kwargs):
    return render(request, "dhr_training_management.html", context=None)


def dhr_performance(request, **kwargs):
    return render(request, "dhr_performance_management.html", context=None)