import os

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from app_blog.models import Blog
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image


class BlogListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create 13 blogs for pagination tests
        number_of_elements = 13
        for element_num in range(number_of_elements):
            Blog.objects.create(description='Christian %s' % element_num, )
            User.objects.create(username='admin%s' % element_num, email='admin@test.com', password='pass')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/blog/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('blog-list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('blog-list'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'app_blog/blog-list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('blog-list'))
        self.assertEqual(resp.status_code, 200)
        self.assertFalse(len(resp.context['Blogs']) == 10)
        self.assertFalse(len(resp.context['Users']) == 10)

    def test_lists_all_authors(self):
        resp = self.client.get(reverse('blog-list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(len(resp.context['Blogs']) == 13)
        self.assertTrue(len(resp.context['Users']) == 13)


class BlogDetailViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Blog.objects.create(description='description')

    def test_view_uses_correct_template(self):
        resp = self.client.get('/blog/blog-detail/1/')
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'app_blog/blog-detail.html')


class AddBlogTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = get_user_model()
        cls.user = user.objects.create_user(
            email='asdf@gmail.com',
            password='hiwa_asdf',
            username='smile',
            last_name='fred',
        )

    def test_add_blog(self):
        self.client = Client()
        self.client.force_login(self.user)
        response = self.client.get(reverse('add-blog'))
        self.assertEqual(response.status_code, 200)
        image = SimpleUploadedFile(name='test_image.jpg', content=open("14hq.png", 'rb').read(),
                                   content_type='image/jpeg')
        response = self.client.post(reverse('add-blog'),
                                    data={'description': 'The Catcher in the Rye', 'images': image},
                                    follow=True)
        blog = Blog.objects.count()
        self.assertEqual(blog, 1)

        # self.assertEqual(response.status_code, 200)

# class UploadBlogTest(TestCase):
#

#     @classmethod
#     def setUpTestData(cls):
#         user = get_user_model()
#         cls.user = user.objects.create_user(
#             email='asdf@gmail.com',
#             password='hiwa_asdf',
#             username='smile',
#             last_name='fred',
#         )
#
#     def test_upload_blog(self):
#         self.client = Client()
#         self.client.force_login(self.user)
#         response = self.client.get(reverse('upload-blog'))
#         self.assertEqual(response.status_code, 200)
#         file_csv = SimpleUploadedFile('test.csv', b"file_content")
#         response = self.client.post(reverse('upload-blog'),
#                                     data={'file': file_csv},
#                                     follow=True)
#         # blog = Blog.objects.count()
#         # self.assertEqual(blog, 2)
