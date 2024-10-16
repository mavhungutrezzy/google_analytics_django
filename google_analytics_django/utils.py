from . import conf


def should_track(request):
    if conf.GOOGLE_ANALYTICS_DEBUG_MODE:
        return False
    if hasattr(request, "user") and request.user.is_staff:
        return False
    return True


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def get_ga_context():
    return {
        "GOOGLE_ANALYTICS_PROPERTY_ID": conf.GOOGLE_ANALYTICS_PROPERTY_ID,
        "GOOGLE_ANALYTICS_DOMAIN": conf.GOOGLE_ANALYTICS_DOMAIN,
        "GOOGLE_ANALYTICS_ANONYMIZE_IP": conf.GOOGLE_ANALYTICS_ANONYMIZE_IP,
        "GOOGLE_ANALYTICS_SAMPLE_RATE": conf.GOOGLE_ANALYTICS_SAMPLE_RATE,
        "GOOGLE_ANALYTICS_SITE_SPEED_SAMPLE_RATE": conf.GOOGLE_ANALYTICS_SITE_SPEED_SAMPLE_RATE,
        "GOOGLE_ANALYTICS_COOKIE_EXPIRES": conf.GOOGLE_ANALYTICS_COOKIE_EXPIRES,
        "GOOGLE_ANALYTICS_DISPLAY_FEATURES": conf.GOOGLE_ANALYTICS_DISPLAY_FEATURES,
    }
