from django import template
from . import vendor as util_vendor

register = template.Library()
Context = template.Context()


@register.simple_tag(takes_context=True)
def meta(context, *args):
    context = (
        '<meta http-equiv="X-UA-Compatible" content="IE=edge">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
    )
    return '\n'.join(context)


@register.simple_tag(takes_context=True)
def vendor(context, *tags):
    return util_vendor(*tags).render()
