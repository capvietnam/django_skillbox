from django.test import TestCase
from app_blog.models import Blog, Images
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Blog.objects.create(description='description')

    def test_description_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_description_max_length(self):
        blog = Blog.objects.get(id=1)
        max_length = blog._meta.get_field('description').max_length
        self.assertEquals(max_length, 500)

    def test_get_absolute_url(self):
        blog = Blog.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(blog.get_absolute_url(), '/blog/blog-detail/1/')

