from django import template
from django.template.loader import render_to_string
from ..utils import get_ga_context, should_track
from .. import conf

register = template.Library()


@register.simple_tag(takes_context=True)
def google_analytics(context):
    request = context["request"]
    if not should_track(request):
        return ""

    ga_context = get_ga_context()
    template_name = (
        "google_analytics/analytics_gtag.html"
        if conf.GOOGLE_ANALYTICS_USE_GTAG
        else "google_analytics/analytics_universal.html"
    )
    return render_to_string(template_name, ga_context)
