from django import template
from django.template.loader import render_to_string
from google_analytics.utils import get_ga_context, should_track

register = template.Library()


@register.simple_tag(takes_context=True)
def google_analytics(context):
    """
    Template tag to include Google Analytics tracking scripts in the rendered template.

    This tag checks if the request should be tracked. If tracking is enabled, it retrieves
    the Google Analytics context settings and renders the appropriate tracking template
    based on the configuration.

    Args:
        context (dict): The template context, which should contain the current request object.

    Returns:
        str: The rendered HTML for Google Analytics tracking scripts, or an empty string if
        tracking is disabled.
    """
    request = context["request"]

    if not should_track(request):
        return ""

    ga_context = get_ga_context()

    template_name = "google_analytics/analytics_gtag.html"

    return render_to_string(template_name, ga_context)
