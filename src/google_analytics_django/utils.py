from google_analytics_django import conf

def should_track(request):
    """
    Determines if a request should be tracked by Google Analytics.

    The request will not be tracked if:
    - Google Analytics debug mode is enabled (`conf.GOOGLE_ANALYTICS_DEBUG_MODE`).
    - The user making the request is a staff member.

    Args:
        request (HttpRequest): The current request object.

    Returns:
        bool: False if the request should not be tracked, True otherwise.
    """
    if conf.GOOGLE_ANALYTICS_DEBUG_MODE:
        return False
    if hasattr(request, "user") and request.user.is_staff:
        return False
    return True

def get_client_ip(request):
    """
    Retrieves the client IP address from the request object.

    It first checks if the 'HTTP_X_FORWARDED_FOR' header is present (common when
    a proxy or load balancer is used), and if not, it falls back to the 'REMOTE_ADDR'
    header.

    Args:
        request (HttpRequest): The current request object.

    Returns:
        str: The client's IP address.
    """
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]  # Get the first IP in the list
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip

def get_ga_context():
    """
    Returns a dictionary containing Google Analytics configuration settings.

    These settings are retrieved from the `conf` module and include:
    - Google Analytics property ID.
    - The domain for Google Analytics tracking.
    - Whether IP anonymization is enabled.
    - Sample rate settings.
    - Cookie expiration settings.
    - Whether display features are enabled.

    Returns:
        dict: A dictionary containing Google Analytics settings for rendering into templates.
    """
    return {
        "GOOGLE_ANALYTICS_PROPERTY_ID": conf.GOOGLE_ANALYTICS_PROPERTY_ID,
        "GOOGLE_ANALYTICS_DOMAIN": conf.GOOGLE_ANALYTICS_DOMAIN,
        "GOOGLE_ANALYTICS_ANONYMIZE_IP": conf.GOOGLE_ANALYTICS_ANONYMIZE_IP,
        "GOOGLE_ANALYTICS_SAMPLE_RATE": conf.GOOGLE_ANALYTICS_SAMPLE_RATE,
        "GOOGLE_ANALYTICS_SITE_SPEED_SAMPLE_RATE": conf.GOOGLE_ANALYTICS_SITE_SPEED_SAMPLE_RATE,
        "GOOGLE_ANALYTICS_COOKIE_EXPIRES": conf.GOOGLE_ANALYTICS_COOKIE_EXPIRES,
        "GOOGLE_ANALYTICS_DISPLAY_FEATURES": conf.GOOGLE_ANALYTICS_DISPLAY_FEATURES,
    }
