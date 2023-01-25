from django.urls import reverse
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from app_users.models import Profile
from PIL import Image


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
            'last_name': 'fred',
            'description': '122',
            'username': 'smile',
            'password2': 'Hhfghfg1223',
            'password1': 'Hhfghfg1223',
        }, follow=True)
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)
        self.assertEqual(getattr(Profile.objects.first(), 'last_name'), 'fred')
        self.assertEqual(getattr(User.objects.first(), 'username'), 'smile')
        self.assertEqual(getattr(Profile.objects.first(), 'description'), '122')


class ProfileTest(TestCase):
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('user-profile'))
        self.assertEqual(resp.status_code, 302)
        resp = self.client.get('/users/profile/')
        self.assertEqual(resp.status_code, 302)

    def test_profile(self):
        self.client = Client()
        response = self.client.post(reverse('user-register'), data={
            'last_name': 'fred',
            'description': '122',
            'username': 'smile',
            'password2': 'Hhfghfg1223',
            'password1': 'Hhfghfg1223',
        }, follow=True)
        avatar = SimpleUploadedFile(name='test_image.jpg', content=open("14hq.png", 'rb').read(),
                                    content_type='image/jpeg')
        response = self.client.post(reverse('user-profile'), data={
            'username': 'smile1',
            'avatar': avatar,
            'description': '1221',
            'last_name': 'fred1',
        }, follow=True)
        user_name = getattr(User.objects.first(), 'username')
        self.assertEqual(user_name, 'smile1')
        last_name_profile = getattr(Profile.objects.first(), 'last_name')
        self.assertEqual(last_name_profile, 'fred1')
        self.assertEqual(getattr(Profile.objects.first(), 'description'), '1221')


class AuthenticationTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = get_user_model()
        cls.user = user.objects.create_user(
            email='asdf@gmail.com',
            password='hiwa_asdf',
            username='smile',
            last_name='fred',
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




