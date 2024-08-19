from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class MainViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.cookies['last_login'] = '2024-08-19 12:34:56'
    
    def test_main_url_redirects_for_anonymous_user(self):
        response = self.client.get(reverse('main:show_main'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/')

    def test_main_url_is_exist_for_authenticated_user(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('main:show_main'))
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template_for_authenticated_user(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('main:show_main'))
        self.assertTemplateUsed(response, 'main.html')
