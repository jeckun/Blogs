from django.shortcuts import render
from ..config import APP_INF


def index(request, *args, **kwargs):
    context = {}
    update_app_inf_nav_menu_current('index')
    context.update(APP_INF)
    return render(request, "base/index.html", context)


def note(request, *args, **kwargs):
    context = {}
    update_app_inf_nav_menu_current('note')
    context.update(APP_INF)
    return render(request, "base/note.html", context)


def example(request, *args, **kwargs):
    context = {}
    update_app_inf_nav_menu_current('example')
    context.update(APP_INF)
    return render(request, "base/example.html", context)


def update_app_inf_nav_menu_current(url_name):
    for item in APP_INF['NAV']['menu']:
        if APP_INF['NAV']['menu'][item]['url'] == url_name:
            APP_INF['NAV']['menu'][item]['current'] = True
        else:
            APP_INF['NAV']['menu'][item]['current'] = False
