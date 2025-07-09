"""Yandex contest of chapter 2.1 of Python course."""


# +
# 1
def task_1() -> None:
    """Task 1."""
    print("Привет, Яндекс!")


task_1()


# +
# 2
def task_2() -> None:
    """Task 2."""
    username: str = input("Как Вас зовут?\n")
    print("Привет,", username)


task_2()


# +
# 3
def task_3() -> None:
    """Task 3."""
    string: str = input()
    print(f"{string}\n" * 3)


task_3()


# +
# 4
def task_4() -> None:
    """Task 4."""
    price: int = int(input())
    print(f"{price - 2.5 * 38:.0f}")


task_4()


# +
# 5
def task_5() -> None:
    """Task 5."""
    price: float = float(input())
    weight: float = float(input())
    amount_of_money: float = float(input())
    print(int(amount_of_money - price * weight))


task_5()


# +
# 6
def task_6() -> None:
    """Task 6."""
    name_of_product: str = input()
    price_per_kg: int = int(input())
    weight: int = int(input())
    customer_balance: int = int(input())
    summary_cost: int = weight * price_per_kg
    change: int = customer_balance - summary_cost

    print(
        "Чек",
        f"{name_of_product} - {weight}кг - {price_per_kg}руб/кг",
        f"Итого: {summary_cost}руб",
        f"Внесено: {customer_balance}руб",
        f"Сдача: {change}руб",
        sep="\n",
    )


task_6()


# +
# 7
def task_7() -> None:
    """Task 7."""
    print(int(input()) * "Купи слона!\n")


task_7()


# +
# 8
def task_8() -> None:
    """Task 8."""
    count_of_strings: int = int(input())
    phrase: str = input()
    print(f'Я больше никогда не буду писать "{phrase}"!\n' * count_of_strings)


task_8()


# +
# 9
def task_9() -> None:
    """Task 9."""
    children_count: int = int(input())
    time: int = int(input())

    print(children_count * time // 2)


task_9()


# +
# 10
def task_10() -> None:
    """Task 10."""
    name: str = input()
    locker_number: int = int(input())

    print(
        f"Группа №{locker_number // 100}.\n"
        f"{locker_number % 10}. {name}.\n"
        f"Шкафчик: {locker_number}.\n"
        f"Кроватка: {locker_number % 100 // 10}."
    )


task_10()


# +
# 11
def task_11() -> None:
    """Task 11."""
    number: int = int(input())

    number1: int = number // 1000
    number2: int = number // 100 % 10
    number3: int = number // 10 % 10
    number4: int = number % 10

    print(number2, number1, number4, number3, sep="")


task_11()


# +
# 12
def task_12() -> None:
    """Task 12."""
    num_a: int = int(input())
    num_b: int = int(input())

    res: int = 0
    mult: int = 1

    while num_a > 0 or num_b > 0:
        da: int = num_a % 10  # младшая цифра a
        db: int = num_b % 10  # младшая цифра b
        num_d: int = (da + db) % 10  # сложение без переноса

        res = res + num_d * mult  # приписали цифру d в правильный разряд
        mult = mult * 10  # переходим к следующему разряду
        num_a = num_a // 10  # «срезали» младший разряд
        num_b = num_b // 10

    print(res)


task_12()


# +
# 13
def task_13() -> None:
    """Task 13."""
    count_of_children: int = int(input())
    count_of_sweets: int = int(input())

    sweets_per_child: int = count_of_sweets // count_of_children
    sweets_remainder: int = count_of_sweets % count_of_children

    print(sweets_per_child, sweets_remainder, sep="\n")


task_13()


# +
# 14
def task_14() -> None:
    """Task 14."""
    red_balls: int = int(input())
    #    green_balls: int = int(input())
    blue_balls: int = int(input())

    print(red_balls + blue_balls + 1)


task_14()


# +
# 15
def task_15() -> None:
    """Task 15."""
    hours: int = int(input())
    minutes: int = int(input())
    time_to_delivery: int = int(input())

    print(
        f"{((time_to_delivery + minutes) // 60 + hours) % 24:02d}:"
        f"{(time_to_delivery + minutes) % 60:02d}"
    )


task_15()


# +
# 16
def task_16() -> None:
    """Task 16."""
    warehouse_km: int = int(input())
    shop_km: int = int(input())
    speed_of_car_km_per_hour = int(input())

    print(f"{(shop_km - warehouse_km) / speed_of_car_km_per_hour:.2f}")


task_16()


# +
# 17
def task_17() -> None:
    """Task 17."""
    summary: int = int(input())
    last_purchase: int = int(input(), 2)
    print(summary + last_purchase)


task_17()


# +
# 18
def task_18() -> None:
    """Task 18."""
    purchase = int(input(), 2)
    customer_wallet = int(input())

    print(customer_wallet - purchase)


task_18()


# +
# 19
def task_19() -> None:
    """Task 19."""
    item: str = input()
    price: int = int(input())
    weight: int = int(input())
    money: int = int(input())

    headings: list[str] = ["Товар:", "Цена:", "Итого:", "Внесено:", "Сдача:"]
    values: list[str] = [
        item,
        f"{weight}кг * {price}руб/кг",
        f"{weight * price}руб",
        f"{money}руб",
        f"{money - weight * price}руб",
    ]

    print("Чек".center(35, "="))
    for idx, heading in enumerate(headings):
        # выравниваем заголовок влево (10), а значение — вправо (25)
        print(f"{heading:<10}{values[idx]:>25}")
    print("=" * 35)


task_19()


# +
# 20
def task_20() -> None:
    """Task 20."""
    n_num: int = int(input())  # общий вес (кг)
    m_num: int = int(input())  # цена смешанного товара (руб/кг)
    k_1: int = int(input())  # цена первого вида котлет (руб/кг)
    k_2: int = int(input())  # цена второго вида котлет (руб/кг), k_2 < k_1

    # x_num - вес первой партии, y_num - вес второй
    x_num = n_num * (m_num - k_2) // (k_1 - k_2)
    y_num = n_num - x_num

    print(x_num, y_num)


task_20()
