from django.test import TestCase, RequestFactory
from django.template import Context, Template
from django.contrib.auth.models import User
from src.google_analytics_django import conf


class GoogleAnalyticsTemplateTagTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.staff_user = User.objects.create_user(
            username="staffuser", password="12345", is_staff=True
        )

    def render_template(self, string, context=None):
        context = context or {}
        context = Context(context)
        return Template(string).render(context)

    def test_google_analytics_tag_renders(self):
        request = self.factory.get("/")
        request.user = self.user
        old_property_id = conf.GOOGLE_ANALYTICS_PROPERTY_ID
        conf.GOOGLE_ANALYTICS_PROPERTY_ID = "UA-TEST-ID"

        rendered = self.render_template(
            "{% load google_analytics_tags %}{% google_analytics %}",
            {"request": request},
        )

        self.assertIn("UA-TEST-ID", rendered)
        self.assertIn("gtag", rendered)

        conf.GOOGLE_ANALYTICS_PROPERTY_ID = old_property_id

    def test_google_analytics_tag_staff_user(self):
        request = self.factory.get("/")
        request.user = self.staff_user

        rendered = self.render_template(
            "{% load google_analytics_tags %}{% google_analytics %}",
            {"request": request},
        )

        self.assertEqual(rendered, "")

    def test_google_analytics_tag_debug_mode(self):
        request = self.factory.get("/")
        request.user = self.user
        old_debug_mode = conf.GOOGLE_ANALYTICS_DEBUG_MODE
        conf.GOOGLE_ANALYTICS_DEBUG_MODE = True

        rendered = self.render_template(
            "{% load google_analytics_tags %}{% google_analytics %}",
            {"request": request},
        )

        self.assertEqual(rendered, "")

        conf.GOOGLE_ANALYTICS_DEBUG_MODE = old_debug_mode
