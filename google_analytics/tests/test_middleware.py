from django.test import TestCase, RequestFactory
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from google_analytics.middleware import GoogleAnalyticsMiddleware
from google_analytics_django import conf

User = get_user_model()


class GoogleAnalyticsMiddlewareTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.middleware = GoogleAnalyticsMiddleware(
            get_response=lambda r: HttpResponse()
        )
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.staff_user = User.objects.create_user(
            username="staffuser", password="12345", is_staff=True
        )

    def test_process_response_adds_headers(self):
        request = self.factory.get("/")
        request.user = self.user
        request.COOKIES["_ga"] = "GA1.2.1234567890.1234567890"

        response = self.middleware(request)

        self.assertIn("X-GA-TRACKING-ID", response)
        self.assertEqual(response["X-GA-TRACKING-ID"], "GA1.2.1234567890.1234567890")
        self.assertIn("X-CLIENT-IP", response)

    def test_process_response_staff_user(self):
        request = self.factory.get("/")
        request.user = self.staff_user

        response = self.middleware(request)

        self.assertNotIn("X-GA-TRACKING-ID", response)
        self.assertNotIn("X-CLIENT-IP", response)

    def test_process_response_debug_mode(self):
        old_debug_mode = conf.GOOGLE_ANALYTICS_DEBUG_MODE
        conf.GOOGLE_ANALYTICS_DEBUG_MODE = True

        request = self.factory.get("/")
        request.user = self.user

        response = self.middleware(request)

        self.assertNotIn("X-GA-TRACKING-ID", response)
        self.assertNotIn("X-CLIENT-IP", response)

        conf.GOOGLE_ANALYTICS_DEBUG_MODE = old_debug_mode
