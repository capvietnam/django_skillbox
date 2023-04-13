
def pop(old_money_spent, money_spent):
    if old_money_spent < (10 ** 4 or 10 ** 5 or 10 ** 6) <= money_spent:
        print(1)
    else:
        print(0)

pop(200, 250)
