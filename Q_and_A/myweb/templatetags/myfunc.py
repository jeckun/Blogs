from django import template

register = template.Library()

"""
    Load a custom template tag library into the parser.

    For example, to load the template tags in
    ``django/templatetags/news/photos.py``::

        {% load news.photos %}

    Can also be used to load an individual tag/filter from
    a library::

    {% load byline from news %}
File "/Users/kun/PycharmProjects/django_test/venv/lib/python3.7/site-packages/django/template/defaulttags.py", 

"""
@register.filter(is_safe=True)
def label_with_classes(value, arg):
    return value.label_tag(attrs={'class': arg})


@register.filter(is_safe=True)
def label_with_type(value, arg):
    return value.label_tag(attrs={'type': arg})
