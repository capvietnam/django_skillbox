from django.test import TestCase
from app_blog.models import Blog
from django.urls import reverse
from django.contrib.auth.models import User


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

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/blog/blog-detail/1/')
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get('/blog/blog-detail/1/')
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'app_blog/blog-detail.html')


class AddBlogTest(TestCase):
    def test_call_view_deny_anonymous(self):
        response = self.client.get(reverse('add-blog'), follow=True)
        self.assertRedirects(response, '/users/login/?next=/blog/add-blog/')
        response = self.client.post(reverse('add-blog'), follow=True)
        self.assertRedirects(response, '/users/login/?next=/blog/add-blog/')

    # def test_add_blog(self):
    #     response = self.client.get(reverse('add-blog'),
    #                                {'description': 'The Catcher in the Rye', 'image': '', 'date_create': ''})
    #     self.assertEqual(response.status_code, 302)
    #     response = self.client.post(reverse('add-blog'),
    #                                 data={'description': 'The Catcher in the Rye', 'image': '', 'date_create': ''},
    #                                 follow=True)
    #
    #     self.assertEqual(response.status_code, 200)
    #     blog = Blog.objects.count()
    #     self.assertEqual(blog, 1)
