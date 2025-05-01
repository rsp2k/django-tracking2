from django import template

from tracking.models import Pageview

register = template.Library()


@register.simple_tag(takes_context=True)
def page_view_count(context, path=None):
    if not path:
        if request := context.get("request"):
            path = request.path
    if path:
        return Pageview.objects.filter(
            url__contains=path,
        ).count()

    return None
