from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class DashboardViewTests(TestCase):
    def test_dashboard_requires_login(self):
        response = self.client.get(reverse("dashboard"))

        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("login"), response["Location"])

    def test_dashboard_renders_for_authenticated_user(self):
        user = User.objects.create_user(username="demo", password="test-pass-123")
        self.client.force_login(user)

        response = self.client.get(reverse("dashboard"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "demo")


class HomeViewTests(TestCase):
    def test_home_redirects_to_dashboard(self):
        response = self.client.get(reverse("home"))

        self.assertRedirects(response, reverse("dashboard"), fetch_redirect_response=False)
