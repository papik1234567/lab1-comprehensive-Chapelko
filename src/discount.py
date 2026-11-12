
import os


def calculate_cart_total(cart_sum, tier, promos):
    price = cart_sum

    # Базовая скидка для крупных заказов.
    if cart_sum > 15000:
        price = cart_sum * 0.85

    # Применение промокодов.
    for promo in promos:
        if promo == "SUMMER":
            price = price - 500
        elif promo == "VIP":
            price = price * 0.90

    # Скидка в зависимости от уровня лояльности.
    if tier == 1:
        price = price * 0.97
    elif tier == 2:
        price = price * 0.93

    # Проверка максимального размера скидки.
    if price < cart_sum * 0.70:
        price = cart_sum * 0.70

    return price


# Эта строка намеренно длиннее установленного ограничения в восемьдесят символов, чтобы проверить работу линтера.
