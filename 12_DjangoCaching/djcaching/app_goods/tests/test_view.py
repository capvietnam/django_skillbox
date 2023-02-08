from django.test import TestCase
from app_goods.models import Shop
from django.urls import reverse


class BlogListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create 13 shop for pagination tests
        number_of_elements = 13
        for element_num in range(number_of_elements):
            Shop.objects.create(title='Christian %s' % element_num, )

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/goods/shop_list/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('shop-list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('shop-list'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'app_goods/shop-list.html')


