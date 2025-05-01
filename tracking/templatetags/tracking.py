from django import template

from tracking.models import Pageview

register = template.Library()


@register.simple_tag(takes_context=True)
def page_view_count(context):
    if request := context.get("request"):
        return Pageview.objects.filter(
            url__contains=request.path,
        ).count()
    return None
