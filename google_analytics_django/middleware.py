from django.utils.deprecation import MiddlewareMixin
from .utils import should_track, get_client_ip


class GoogleAnalyticsMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if should_track(request):
            ga_cookie = request.COOKIES.get("_ga")
            if ga_cookie:
                response["X-GA-TRACKING-ID"] = ga_cookie
            response["X-CLIENT-IP"] = get_client_ip(request)
        return response
