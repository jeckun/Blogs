"""newtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from blog.views import PostViews, example, bootstrap, dhr_index, dhr_org, \
    dhr_emp, dhr_job_adj, dhr_time, dhr_leave, dhr_overtime, dhr_trip, dhr_benefit, \
    dhr_payroll, dhr_recruitment, dhr_training, dhr_performance


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('dhr/', dhr_index, name='dhr'),
    path('dhr/org/', dhr_org, name='org'),
    path('dhr/emp/', dhr_emp, name='emp'),
    path('dhr/job/', dhr_job_adj, name='job'),
    path('dhr/time/', dhr_time, name='time'),
    path('dhr/leave/', dhr_leave, name='leave'),
    path('dhr/overtime/', dhr_overtime, name='overtime'),
    path('dhr/trip/', dhr_trip, name='trip'),
    path('dhr/benefit/', dhr_benefit, name='benefit'),
    path('dhr/payroll/', dhr_payroll, name='payroll'),
    path('dhr/recruitment/', dhr_recruitment, name='recruitment'),
    path('dhr/training/', dhr_training, name='training'),
    path('dhr/performance/', dhr_performance, name='performance'),
    # url(r'^dhr/$', dhr_index, name='dhr'),
    # url(r'^dhr/org/$', dhr_org, name='org'),
    # url(r'^dhr/emp/', dhr_emp, name='emp'),
    # url(r'^dhr/job/', dhr_job_adj, name='job'),
    url(r'^$', PostViews.as_view(), name='Post'),
    url(r'^example/', example, name='example'),
    url(r'^bootstrap/', bootstrap, name='bootstrap'),
    url(r'^admin/', admin.site.urls, name='admin'),
]
