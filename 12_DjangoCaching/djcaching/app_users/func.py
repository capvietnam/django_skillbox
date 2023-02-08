import random
from app_goods.models import Goods


def get_random_good(good_id):
    promotion_good = Goods.objects.get(id=good_id)
    return promotion_good


def get_good_prise(good_id):
    promotion_prise = Goods.objects.get(id=good_id).price * 9 / 10
    return promotion_prise
