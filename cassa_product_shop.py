def print_menu(prices):
    print("Товары в продаже:")
    for product, price in prices.items():
        print(f"  {product} — {price} руб.")


def ask_quantity(product):
    while True:
        raw = input(f"Сколько «{product}»? ")
        try:
            quantity = int(raw)
        except ValueError:
            print("Введите целое положительное число.")
            continue
        if quantity <= 0:
            print("Количество должно быть больше нуля.")
            continue
        return quantity


def item_cost(price, quantity):
    return price * quantity


def calculate_total(cart):
    total = 0
    for product, quantity, cost in cart:
        total += cost
    return total


def print_receipt(cart):
    for number, (product, quantity, cost) in enumerate(cart, start=1):
        print(f"{number}. {product} × {quantity} = {cost} руб.")
    total = calculate_total(cart)
    print(f"Сумма: {total} руб.")
    return total


def apply_discount(total, card=False):
    if card:
        discount = total * 10 // 100
    elif total >= 1000:
        discount = total * 5 // 100
    else:
        discount = 0
    return discount, total - discount


def ask_card():
    while True:
        answer = input("Есть карта магазина? (да/нет): ").strip().lower()
        if answer in ("да", "нет"):
            return answer == "да"
        print("Введите «да» или «нет».")


def main():
    prices = {
        "хлеб": 50,
        "молоко": 90,
        "сыр": 400,
        "яблоки": 120,
        "кофе": 350
    }

    cashier_name = input("Введите имя кассира: ").strip() or "кассир"
    print(f"Здравствуйте, {cashier_name}! Касса открыта")

    print_menu(prices)

    cart = []

    while True:
        print()
        raw_product = input('Товар (или "оплата", чтобы перейти к оплате): ')
        product = raw_product.strip().lower()

        if product == "оплата":
            if not cart:
                print("Корзина пуста. Добавьте хотя бы один товар.")
                continue
            break

        if product not in prices:
            print(f"Товара «{product}» нет в продаже")
            continue

        quantity = ask_quantity(product)
        cost = item_cost(prices[product], quantity)
        cart.append((product, quantity, cost))
        print(f"Добавлено: {product} × {quantity} = {cost} руб.")

    print()
    has_card = ask_card()

    print()
    print("--- Чек ---")
    total = print_receipt(cart)

    discount, payable = apply_discount(total, card=has_card)

    print(f"Скидка: {discount} руб.")
    print(f"К оплате: {payable} руб.")

    unique_products = {product for product, _, _ in cart}
    print(f"Разных товаров в чеке: {len(unique_products)}")

    print()
    print(f"Спасибо за работу, {cashier_name}!")


if __name__ == "__main__":
    main()