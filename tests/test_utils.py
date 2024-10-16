from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from google_analytics_django import utils, conf


class GoogleAnalyticsUtilsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.staff_user = User.objects.create_user(
            username="staffuser", password="12345", is_staff=True
        )

    def test_should_track(self):
        request = self.factory.get("/")
        request.user = self.user

        self.assertTrue(utils.should_track(request))

    def test_should_not_track_staff(self):
        request = self.factory.get("/")
        request.user = self.staff_user

        self.assertFalse(utils.should_track(request))

    def test_should_not_track_debug_mode(self):
        request = self.factory.get("/")
        request.user = self.user
        old_debug_mode = conf.GOOGLE_ANALYTICS_DEBUG_MODE
        conf.GOOGLE_ANALYTICS_DEBUG_MODE = True

        self.assertFalse(utils.should_track(request))

        conf.GOOGLE_ANALYTICS_DEBUG_MODE = old_debug_mode

    def test_get_client_ip(self):
        request = self.factory.get("/")
        request.META["REMOTE_ADDR"] = "127.0.0.1"

        self.assertEqual(utils.get_client_ip(request), "127.0.0.1")

    def test_get_client_ip_x_forwarded_for(self):
        request = self.factory.get("/")
        request.META["HTTP_X_FORWARDED_FOR"] = "10.0.0.1, 10.0.0.2"

        self.assertEqual(utils.get_client_ip(request), "10.0.0.1")

    def test_get_ga_context(self):
        context = utils.get_ga_context()

        self.assertIn("GOOGLE_ANALYTICS_PROPERTY_ID", context)
        self.assertIn("GOOGLE_ANALYTICS_DOMAIN", context)
        self.assertIn("GOOGLE_ANALYTICS_ANONYMIZE_IP", context)
        self.assertIn("GOOGLE_ANALYTICS_SAMPLE_RATE", context)
        self.assertIn("GOOGLE_ANALYTICS_SITE_SPEED_SAMPLE_RATE", context)
        self.assertIn("GOOGLE_ANALYTICS_COOKIE_EXPIRES", context)
        self.assertIn("GOOGLE_ANALYTICS_DISPLAY_FEATURES", context)
