import random
from app_goods.models import Goods, Shop
from django.contrib.auth.models import User
from django.db.models import F
from faker import Faker
from app_users.models import Profile, Sale

fake = Faker()


def check_stutus(old_money_spent, money_spent):
    if old_money_spent < 10 ** 4 <= money_spent:
        return True
    elif old_money_spent < 10 ** 5 <= money_spent:
        return True
    elif old_money_spent < 10 ** 6 <= money_spent:
        return True


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

# def create_all_models(num_profiles):
#     for i in range(num_profiles):
#         user = User.objects.create_user(
#             username=fake.user_name(),
#             email=fake.email(),
#             password=fake.password()
#         )
#         profile = Profile.objects.create(
#             user=user,
#             balance=fake.pyint(min_value=0, max_value=100000),
#             money_spent=fake.pyint(min_value=0, max_value=100000),
#         )
#         shop = Shop.objects.create(
#             title=fake.text(),
#         )
#         goods = Goods.objects.create(
#             shop=shop,
#             title=fake.text(),
#             price=fake.pyint(min_value=0, max_value=1000),
#             description=fake.text(),
#             rest_goods=fake.pyint(min_value=0, max_value=100),
#         )
#         sale = Sale.objects.create(
#             user=user,
#             goods=goods,
#             quantity=fake.pyint(min_value=0, max_value=1000),
#         )
#
# create_all_models(2500)
