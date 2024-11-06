from django.utils.deprecation import MiddlewareMixin
from .utils import should_track, get_client_ip


class GoogleAnalyticsMiddleware(MiddlewareMixin):
    """
    Middleware to append Google Analytics tracking ID and client IP address
    to the response headers for requests that should be tracked.

    This middleware checks if a request should be tracked (using the `should_track` function).
    If tracking is enabled, it retrieves the Google Analytics cookie and appends the tracking ID
    and client IP address to the response headers.
    """

    def process_response(self, request, response):
        """
        Modify the response to include Google Analytics tracking ID and client IP address
        if tracking is enabled for the current request.

        Args:
            request (HttpRequest): The current request object.
            response (HttpResponse): The response object to be modified.

        Returns:
            HttpResponse: The modified response object with additional headers, if applicable.
        """
        if should_track(request):
            ga_cookie = request.COOKIES.get("_ga")

            if ga_cookie:
                response["X-GA-TRACKING-ID"] = ga_cookie

            response["X-CLIENT-IP"] = get_client_ip(request)

        return response
