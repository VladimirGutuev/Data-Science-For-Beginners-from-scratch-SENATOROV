"""Yandex contest of chapter 2.3 of Python course."""

# +
# 1
shout: str

while (shout := input()) != "Три!":
    print("Режим ожидания...")
print("Ёлочка, гори!")
# -

# 2
counter: int = 0
string: str
while (string := input()) != "Приехали!":
    if "зайка" in string:
        counter += 1
print(counter)


# +
# 3
def task_3() -> None:
    """Task 23."""
    first_number: int = int(input())
    second_number: int = int(input())
    for i in range(first_number, second_number + 1):
        print(i, end=" ")


task_3()


# +
# 4
def task_4() -> None:
    """Task 4."""
    first_number: int = int(input())
    second_number: int = int(input())
    if first_number < second_number:
        for i in range(first_number, second_number + 1):
            print(i, end=" ")
    else:
        for i in range(first_number, second_number - 1, -1):
            print(i, end=" ")


task_4()


# +
# 5
def task_5() -> None:
    """Task 5."""
    price_of_product: float
    summary: float = 0

    while (price_of_product := float(input())) != 0:
        if price_of_product >= 500:
            summary += price_of_product * 0.9
        else:
            summary += price_of_product
    print(f"{summary:.1f}")


task_5()


# +
# 6
def task_6() -> None:
    """Task 6."""
    first_number: int = int(input())
    second_number: int = int(input())
    remainder: int = 100  # anything number, but not zero
    temp: int = 0  # anything number

    if first_number > second_number:
        while remainder != 0:
            remainder = first_number % second_number
            temp = second_number
            first_number = second_number
            second_number = remainder
        print(temp)
    else:
        while remainder != 0:
            remainder = second_number % first_number
            temp = first_number
            second_number = first_number
            first_number = remainder
        print(temp)


task_6()


# +
# 7
def task_7() -> None:
    """Task 7."""
    first_number: int = int(input())
    second_number: int = int(input())
    step_value: int = first_number if first_number > second_number else second_number
    least_common_multiple: int = step_value

    # ищем ЛКМ, пока оба условия не будут выполнены
    while True:
        if least_common_multiple % first_number != 0:
            least_common_multiple += step_value
            continue

        if least_common_multiple % second_number != 0:
            least_common_multiple += step_value
            continue

        break

    print(least_common_multiple)


task_7()


# +
# 8
def task_8() -> None:
    """Task 8."""
    useful_string: str = input()
    number_of_repetitions: int = int(input())

    for _ in range(number_of_repetitions):
        print(useful_string)


task_8()


# +
# 9
def task_9() -> None:
    """Task 9."""
    number: int = int(input())
    product: int = 1
    for i in range(1, number + 1):
        product *= i
    print(product)


task_9()


# +
# 10
def task_10() -> None:
    """Task 10."""
    direction: str
    scalar: int
    x_dir: int = 0
    y_dir: int = 0

    while (direction := input()) != "СТОП":
        scalar = int(input())
        if direction == "СЕВЕР":
            y_dir += scalar
        elif direction == "ЮГ":
            y_dir -= scalar
        elif direction == "ВОСТОК":
            x_dir += scalar
        else:
            x_dir -= scalar
    print(y_dir, x_dir, sep="\n")


task_10()


# +
# 11
def task_11() -> None:
    """Task 11."""
    initial_number: int = int(input())
    sum_of_digits: int = 0
    remaining_number: int = initial_number

    # пока есть цифры в числе
    while remaining_number > 0:
        current_digit: int = remaining_number % 10
        sum_of_digits += current_digit
        remaining_number //= 10

    print(sum_of_digits)


task_11()


# +
# 12
def task_12() -> None:
    """Task 12."""
    initial_number: int = int(input())
    maximum_digit: int = 0
    remaining_number: int = initial_number

    # перебираем все цифры числа
    while remaining_number > 0:
        current_digit: int = remaining_number % 10
        maximum_digit = max(maximum_digit, current_digit)
        remaining_number //= 10

    print(maximum_digit)


task_12()


# +
# 13
def task_13() -> None:
    """Task 13."""
    player_count: int = int(input())
    minimal_name: str = input()

    for _ in range(player_count - 1):
        current_name: str = input()
        minimal_name = min(minimal_name, current_name)

    print(minimal_name)


task_13()


# +
# 14
def task_14() -> None:
    """Task 14."""
    initial_number: int = int(input())
    if initial_number <= 1:
        print("NO")
        return

    for potential_divisor in range(2, initial_number):
        if initial_number % potential_divisor == 0:
            print("NO")
            break
    else:
        print("YES")


task_14()


# +
# 15
def task_15() -> None:
    """Task 15."""
    total_locations: int = int(input())
    lines_with_rabbit: int = 0

    for _ in range(total_locations):
        current_line: str = input()
        # разбиваем на слова и проверяем точное совпадение
        if "зайка" in current_line.split():
            lines_with_rabbit += 1

    print(lines_with_rabbit)


task_15()


# +
# 16
def task_16() -> None:
    """Task 16."""
    original_number: int = int(input())
    working_number: int = original_number
    reversed_number: int = 0

    # строим перевёрнутое число с помощью while
    while working_number > 0:
        current_digit: int = working_number % 10
        reversed_number = reversed_number * 10 + current_digit
        working_number //= 10

    if reversed_number == original_number:
        print("YES")
    else:
        print("NO")


task_16()


# +
# 17
def task_17() -> None:
    """Task 17."""
    initial_number: int = int(input())
    working_number: int = initial_number
    reversed_filtered: int = 0

    # собираем все нечётные цифры в обратном порядке
    while working_number > 0:
        last_digit: int = working_number % 10
        if last_digit % 2 != 0:
            reversed_filtered = reversed_filtered * 10 + last_digit
        working_number //= 10

    filtered_number: int = 0

    # переворачиваем обратно, чтобы восстановить исходный порядок
    while reversed_filtered > 0:
        last_digit = reversed_filtered % 10
        filtered_number = filtered_number * 10 + last_digit
        reversed_filtered //= 10

    print(filtered_number)


task_17()


# +
# 18
def task_18() -> None:
    """Task 18."""
    original_number: int = int(input())
    remaining: int = original_number
    divisor: int = 2
    first_factor: bool = True

    while remaining > 1:
        if remaining % divisor == 0:
            # выводим либо без звёздочки (первый множитель), либо с " * "
            if first_factor:
                print(divisor, end="")
                first_factor = False
            else:
                print(f" * {divisor}", end="")
            remaining //= divisor
        else:
            divisor += 1

    print()  # перевод на новую строку после всех множителей


task_18()


# +
# 19
def task_19() -> None:
    """Task 19."""
    lower_bound: int = 1
    upper_bound: int = 1000
    attempts: int = 0

    # пока не исчерпали 10 попыток
    while attempts < 10:
        # делаем пробную догадку — середина текущего интервала
        guess: int = (lower_bound + upper_bound) // 2
        # выводим её и сразу сбрасываем буфер, чтобы интерактивно получить
        # ответ
        print(guess, flush=True)
        # читаем ответ: «Больше», «Меньше» или «Угадал!»
        response: str = input()
        if response == "Угадал!":
            print("Число отгадано")
            return
        if response == "Больше":
            # если загаданное число больше нашей догадки —
            # сужаем интервал слева
            lower_bound = guess + 1
        elif response == "Меньше":
            # если загаданное число меньше нашей догадки —
            # сужаем интервал справа
            upper_bound = guess - 1
        attempts += 1

    # на всякий случай можно добавить завершающий вывод
    print("Не удалось угадать за 10 попыток")


task_19()


# +
# 20
def task_20() -> None:
    """Task 20."""
    block_count: int = int(input())
    previous_hash: int = 0

    for block_index in range(block_count):
        block_value: int = int(input())
        hash_value: int = block_value % 256
        random_value: int = (block_value // 256) % 256
        message_value: int = block_value // (256 * 256)

        expected_hash: int = (37 * (message_value + random_value + previous_hash)) % 256

        # если хэш не соответствует формуле или не меньше 100 — это первая
        # ошибка
        if hash_value != expected_hash or hash_value >= 100:
            print(block_index)
            return

        previous_hash = hash_value

    print(-1)


task_20()
