from django.urls import reverse
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from app_users.models import Profile


class AuthenticationTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = get_user_model()
        cls.user = user.objects.create_user(
            password='hiwa_asdf',
            username='smile',
        )

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('user-login'))
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get('/users/login/')
        self.assertEqual(resp.status_code, 200)

    def test_authentication(self):
        self.client = Client()
        response = self.client.post(reverse('user-login'), data={
            'username': 'smile',
            'password': 'hiwa_asdf',
        }, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)


class RegisterTest(TestCase):
    def test_url_login(self):
        resp = self.client.get('/users/register/')
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get(reverse('user-register'))
        self.assertEqual(resp.status_code, 200)

    def test_login(self):
        self.client = Client()
        # send login data
        response = self.client.post(reverse('user-register'), data={
            'username': 'smile',
            'password2': 'Hhfghfg1223',
            'password1': 'Hhfghfg1223',
        }, follow=True)
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)
        self.assertEqual(getattr(User.objects.first(), 'username'), 'smile')


class ProfileTest(TestCase):
    def test_view_uses_correct_template(self):
        self.client = Client()
        response = self.client.post(reverse('user-login'), data={
            'username': 'smile',
            'password': 'hiwa_asdf',
        }, follow=True)
        resp = self.client.get('/users/profile/1')
        self.assertEqual(resp.status_code, 301)
