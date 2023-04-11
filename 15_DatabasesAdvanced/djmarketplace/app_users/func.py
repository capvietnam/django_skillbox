import random
from app_goods.models import Goods
from django.contrib.auth.models import User
from django.db.models import F

def get_ststus(id_user):
    if User.objects.get(id=id_user).profile.money_spent >= 10 ** 6:
        return 3
    if User.objects.get(id=id_user).profile.money_spent >= 10 ** 5:
        return 2
    if User.objects.get(id=id_user).profile.money_spent >= 10 ** 4:
        return 1
    else:
        return 0

def get_random_good(good_id: int) -> list:
    """
    Получает объект товара по id из базы данных
    :param good_id: id товара
    :type good_id: int
    :return: товар
    :rtype: <class 'app_goods.models.Goods'>
    """
    promotion_good = Goods.objects.get(id=good_id)
    print(type(promotion_good))
    return promotion_good


def get_good_prise(good_id: int) -> float:
    """
    Получает цену товара (по id из базы данных) и вычитает 10 процентов товара
    :param good_id: id товара
    :type good_id: int
    :return: товар
    :rtype: float
    """
    promotion_prise = Goods.objects.get(id=good_id).price * 9 / 10
    return promotion_prise

