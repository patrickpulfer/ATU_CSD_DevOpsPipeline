from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class HomeView_TestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'test@test.com', 'testpassword')
        self.home_url = reverse('home')

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 302)

    def test_no_redirect_if_logged_in(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)