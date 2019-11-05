from django import template
from django.utils.safestring import mark_safe
from django.forms.renderers import get_default_renderer
# 加载App配置文件
from ..config import APP_INF

register = template.Library()
Context = template.Context()


@register.simple_tag(takes_context=True)  # 注册get_meta为一个标签
def get_meta(context, *args):
    """ 生成网页meta标签 """
    meta = APP_INF['META']
    context = ['<meta charset="utf-8">',
               '<meta http-equiv="X-UA-Compatible" content="IE=edge">',
               '<meta name="viewport" content="width=device-width, initial-scale=1">',
               ]
    context += ['<meta name=\"%s\" content=\"%s\">' % (a, meta['%s' % a]) for a in meta]
    return mark_safe('\n'.join(context))  # Django不允许直接返回HTML，需要使用mark_safe返回安全字符串


@register.simple_tag(takes_context=True)
def get_brand(context, *args):
    context = '<a class=\"navbar-brand\" href=\"%s\">%s</a>' % (APP_INF['NAV']['brand']['url'],
                                                            APP_INF['NAV']['brand']['content'])
    return mark_safe(context)


@register.simple_tag(takes_context=True)
def get_search(context, *args):
    context = '<form class="navbar-form form-inline navbar-left" role="search">\n'
    context += '<input class="form-control mr-sm-2" type="text" placeholder="查找内容" aria-label="查找内容">\n'
    context += '<button class="btn btn-outline-success" type="submit">查询</button>\n'
    context += '</form>\n'
    return mark_safe(context)


@register.simple_tag(takes_context=True)
def get_pages(context, *args):
    return render('widgets/pages.html', context=context)


@register.simple_tag(takes_context=True)
def nav(context, *args):
    """ 生成顶部导航条 """
    return render('widgets/navbar.html', context=context)


def render(template_name, context, renderer=None):
    if context is not None and not isinstance(context, dict):
        d = {}
        {d.update(c) for c in context.dicts}
        context = d.copy()
    if renderer is None:
        renderer = get_default_renderer()
    return mark_safe(renderer.render(template_name, context))
