
def calculate_cart_total(cart_sum, tier, promos):
    # Начальная стоимость корзины.
    price = cart_sum

    # Базовая скидка 15% для заказов свыше 15000.
    if cart_sum > 15000:
        price = cart_sum * 0.85

    # Последовательное применение промокодов.
    for promo in promos:
        if promo == "SUMMER":
            price = price - 500
        elif promo == "VIP":
            price = price * 0.90

    # Применение скидки по уровню лояльности.
    if tier == 1:
        price = price * 0.97
    elif tier == 2:
        price = price * 0.93

    # Ограничение максимальной скидки значением 30%.
    if price < cart_sum * 0.70:
        price = cart_sum * 0.70

    # Возврат итоговой стоимости корзины.
    return price
