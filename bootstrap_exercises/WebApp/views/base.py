from django.shortcuts import render


def bootstrap(request, **kwargs):
    return render(request, "bootstrap.html", context=None)


def bootstrap_table(request, **kwargs):
    return render(request, "bootstrap_table.html", context=None)

