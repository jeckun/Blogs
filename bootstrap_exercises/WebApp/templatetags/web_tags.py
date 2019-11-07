import datetime
from django import template
from django.utils.safestring import mark_safe
from django.forms.renderers import get_default_renderer
# 加载App配置文件
from ..config import APP_INF
from ..models import Post, Tag

register = template.Library()
Context = template.Context()


@register.filter(name='tag')
def tag(post):
    """ 从post中提取tag并返回tag名称数组 """
    p = post.tag.all()
    return [t.tag for t in p]


@register.filter(name='get_tag_num')
def get_tag_num(tag):
    """ 从post中统计tag出现的次数 """
    return len([a.title for a in Post.objects.all() if Tag.objects.get(tag=tag) in a.tag.all()])


@register.filter(name='get_user_num')
def get_user_num(user):
    """ 从post中统计tag出现的次数 """
    return len([u for u in Post.objects.all() if u.owner==user])


@register.filter(name='get_archive_num')
def get_archive_num(archive):
    return len([u for u in Post.objects.all() if u.archive()==archive])


@register.simple_tag(takes_context=True)
def get_month(context, *args):
    today = datetime.date.today()
    a = today.strftime("%Y-%m")
    return today.strftime("%Y-%m")


@register.simple_tag(takes_context=True)
def get_last_month(context, *args):
    today = datetime.date.today()
    last_month = today + datetime.timedelta(days=-today.day)
    a = last_month.strftime("%Y-%m")
    return last_month.strftime("%Y-%m")


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
    """ 生成品牌标志 """
    context = '<a class=\"navbar-brand\" href=\"%s\">%s</a>' % (APP_INF['NAV']['brand']['url'],
                                                            APP_INF['NAV']['brand']['content'])
    return mark_safe(context)


@register.simple_tag(takes_context=True)
def get_search(context, *args):
    """ 生成查询框 """
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
