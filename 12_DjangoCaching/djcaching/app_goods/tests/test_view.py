from django.test import TestCase
from app_goods.models import Shop
from django.urls import reverse

"""Тесты приложения app_goods"""


class BlogListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Первоначальное создание"""
        # Create 13 shop for pagination tests
        number_of_elements = 13
        for element_num in range(number_of_elements):
            Shop.objects.create(title='Christian %s' % element_num, )

    def test_view_url_exists_at_desired_location(self):
        """Тест url"""
        resp = self.client.get('/goods/shop_list/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """Тест url"""
        resp = self.client.get(reverse('shop-list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        """Тест template"""
        resp = self.client.get(reverse('shop-list'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'app_goods/shop-list.html')
