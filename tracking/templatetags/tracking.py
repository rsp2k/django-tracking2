from django import template

from tracking.models import Pageview

register = template.Library()


@register.simple_tag(takes_context=True)
def page_view_count(context):
    if context.request.path:
        return Pageview.objects.filter(
            url__contains=context.request.path,
        ).count()
