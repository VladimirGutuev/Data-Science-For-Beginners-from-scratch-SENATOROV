"""Yandex contest of chapter 2.4 of Python course."""


# +
# 1
def task_1() -> None:
    """Task 1: выводит таблицу умножения размера n × n."""
    size: int = int(input())

    for row in range(1, size + 1):
        for col in range(1, size + 1):
            product: int = row * col
            if col < size:
                print(product, end=" ")
            else:
                print(product, end="")
        print()


task_1()


# +
# 2
def task_2() -> None:
    """Task 2: выводит список выражений таблицы умножения размера n × n."""
    size: int = int(input())
    multiplier: int
    multiplicand: int
    product: int = 0

    for multiplier in range(1, size + 1):
        for multiplicand in range(1, size + 1):
            product = multiplicand * multiplier
            print(f"{multiplicand} * {multiplier} = {product}")


task_2()


# +
# 3
def task_3() -> None:
    """Task 3: строит «математическую ёлку» из n_nums чисел."""
    n_nums: int = int(input())
    current_number: int = 1
    row_length: int = 1
    pos_in_row: int

    # пока не исчерпали все числа от 1 до n_nums
    while current_number <= n_nums:
        pos_in_row = 1
        # печатаем строку: row_length чисел (или столько, сколько осталось)
        while pos_in_row <= row_length and current_number <= n_nums:
            print(current_number, end=" ")
            current_number += 1
            pos_in_row += 1

        print()  # перевод строки после каждой «ветки» ёлки
        row_length += 1


task_3()


# +
# 4
def task_4() -> None:
    """Task 4: считает сумму цифр всех введённых чисел."""
    count: int = int(input())
    total: int = 0

    for _ in range(count):
        digits: str = input().strip()
        for ch in digits:
            total += int(ch)

    print(total)


task_4()


# +
# 5
def task_5() -> None:
    """Task 5: считает, в скольких местностях встречается 'зайка'."""
    regions_count: int = int(input())
    regions_with_rabbit: int = 0

    for _ in range(regions_count):
        found_rabbit: bool = False
        while True:
            word: str = input()
            if word == "ВСЁ":
                break
            if word == "зайка":
                found_rabbit = True
        if found_rabbit:
            regions_with_rabbit += 1

    print(regions_with_rabbit)


task_5()


# +
# 6
def task_6() -> None:
    """Task 6: находит НОД всех введённых чисел (Алгоритм Евклида)."""
    count: int = int(input())
    result: int = int(input())
    next_number: int
    a_num: int
    b_num: int

    for _ in range(count - 1):
        next_number = int(input())
        # вычисляем gcd(result, next_number)
        a_num = result
        b_num = next_number
        while b_num != 0:
            a_num, b_num = b_num, a_num % b_num
        result = a_num

    print(result)


task_6()


# +
# 7
def task_7() -> None:
    """Task 7: симулирует отсчёт старта для каждого из участников велогонки."""
    participants_count: int = int(input())
    participant_idx: int
    current_countdown: int = 0
    second: int

    for participant_idx in range(1, participants_count + 1):
        # первый участник: 3, второй: 4, третий: 5… то есть 2 + номер участника
        current_countdown = participant_idx + 2
        for second in range(current_countdown, 0, -1):
            print(f"До старта {second} секунд(ы)")
        print(f"Старт {participant_idx}!!!")


task_7()


# +
# 8
def task_8() -> None:
    """Task 8: определяет победителя по максимальной сумме цифр числа."""
    count: int = int(input())
    winner_name: str = ""
    max_sum: int = -1

    for _ in range(count):
        name: str = input().strip()
        digits: str = input().strip()
        sum_of_digits: int = 0
        digit: str

        for digit in digits:
            sum_of_digits += int(digit)

        # при равенстве побеждает тот, кто ходил позже
        if sum_of_digits >= max_sum:
            max_sum = sum_of_digits
            winner_name = name

    print(winner_name)


task_8()


# +
# 9
def task_9() -> None:
    """Task 9: собирает число из максимальных цифр каждого введённого числа."""
    count: int = int(input())
    result: int = 0
    number_str: str
    max_digit: int

    for _ in range(count):
        number_str = input().strip()
        # находим максимальную цифру через max() по символам
        max_digit = max(int(ch) for ch in number_str)
        # сдвигаем ранее собранное число влево и добавляем новую цифру
        result = result * 10 + max_digit

    print(result)


task_9()


# +
# 10
def task_10() -> None:
    """Task 10: все способы распределения N долек апельсина."""
    total_slices: int = int(input())
    anya: int
    borya: int
    vova: int

    # Заголовок
    print("А Б В")

    # Аня получает от 1 до total_slices−2 долек
    for anya in range(1, total_slices - 1):
        # Боря получает от 1 до так, чтобы у Вовы осталась хотя бы 1 долька
        for borya in range(1, total_slices - anya):
            vova = total_slices - anya - borya
            if vova >= 1:
                print(anya, borya, vova)


task_10()


# +
# 11
def task_11() -> None:
    """Task 11: считает количество простых чисел среди введённых."""
    count: int = int(input())
    primes_count: int = 0
    number: int
    divisor: int
    divisors_found: int

    # для каждого из count чисел
    for _ in range(count):
        number = int(input())
        # простые числа — единственные с двумя делителями (1 и само число)
        divisors_found = 0
        # считаем делители от 1 до number
        for divisor in range(1, number + 1):
            if number % divisor == 0:
                divisors_found += 1
        if divisors_found == 2:
            primes_count += 1

    print(primes_count)


task_11()


# +
# 12
def task_12() -> None:
    """Task 12: выводит прямоугольник из чисел столбцами одинаковой ширины."""
    rows: int = int(input())
    cols: int = int(input())
    max_value: int = rows * cols
    col_width: int = len(str(max_value))

    row: int
    col: int
    value: int

    for row in range(1, rows + 1):
        for col in range(1, cols + 1):
            value = (row - 1) * cols + col
            # ровно col_width символов, выравнивание вправо
            if col < cols:
                print(f"{value:>{col_width}}", end=" ")
            else:
                print(f"{value:>{col_width}}", end="")
        print()


task_12()


# +
# 13
def task_13() -> None:
    """Task 13: получаем прямоугольник по столбцам и выровненными столбцами."""
    rows: int = int(input())
    cols: int = int(input())
    max_value: int = rows * cols
    width: int = len(str(max_value))
    r_numb: int
    c_numb: int
    value: int

    for r_numb in range(1, rows + 1):
        for c_numb in range(1, cols + 1):
            value = (c_numb - 1) * rows + r_numb
            if c_numb < cols:
                print(f"{value:>{width}}", end=" ")
            else:
                print(f"{value:>{width}}", end="")
        print()


task_13()


# +
# 14
def task_14() -> None:
    """Task 14: числовая «змейка» размера n × m."""
    rows: int = int(input())
    cols: int = int(input())
    max_value: int = rows * cols
    col_width: int = len(str(max_value))
    r_num: int
    c_num: int
    value: int

    for r_num in range(1, rows + 1):
        if r_num % 2 != 0:
            # нечётная строка: слева направо
            for c_num in range(1, cols + 1):
                value = (r_num - 1) * cols + c_num
                if c_num < cols:
                    print(f"{value:>{col_width}}", end=" ")
                else:
                    print(f"{value:>{col_width}}", end="")
        else:
            # чётная строка: справа налево
            for c_num in range(cols, 0, -1):
                value = (r_num - 1) * cols + c_num
                if c_num > 1:
                    print(f"{value:>{col_width}}", end=" ")
                else:
                    print(f"{value:>{col_width}}", end="")
        print()


task_14()


# +
# 15
def task_15() -> None:
    """Task 15: вертикальная числовая змейка размера N×M."""
    rows: int = int(input())
    cols: int = int(input())
    total: int = rows * cols
    width: int = len(str(total))
    value: int

    for r_num in range(rows):
        for c_num in range(cols):
            base: int = c_num * rows
            if c_num % 2 == 0:
                # чётный столбец (0, 2, …) — сверху вниз
                value = base + r_num + 1
            else:
                # нечётный столбец (1, 3, …) — снизу вверх
                value = base + (rows - r_num)
            if c_num < cols - 1:
                print(f"{value:>{width}}", end=" ")
            else:
                print(f"{value:>{width}}", end="")
        print()


task_15()


# +
# 16
def task_16() -> None:
    """Task 16: таблица умножения с ячейками одинаковой ширины и рамками."""
    size: int = int(input())
    col_width: int = int(input())
    # общая длина строки: size ячеек по col_width и (size−1) разделителей '|'
    line_length: int = size * col_width + (size - 1)
    row: int
    col: int

    for row in range(1, size + 1):
        for col in range(1, size + 1):
            # печатаем число, центрируем в поле ширины col_width
            # разделитель '|' идёт только между ячейками
            print(f"{row * col:^{col_width}}", end="" if col == size else "|")
        print()
        # после каждой строки, кроме последней, рисуем горизонтальную линию
        if row < size:
            print("-" * line_length)


task_16()


# +
# 17
def task_17() -> None:
    """Task 17: считает, сколько введённых чисел являются палиндромами."""
    count: int = int(input())
    palindromes: int = 0
    s_num: str

    for _ in range(count):
        s_num = input()
        # число — палиндром, если строка читается одинаково в обе стороны
        if s_num == s_num[::-1]:
            palindromes += 1

    print(palindromes)


task_17()


# +
# 18
def task_18() -> None:
    """Task 18: строит ёлку из чисел и центрирует каждую строку по ширине."""
    total: int = int(input())
    lines: list[str] = []
    current: int = 1
    row_len: int = 1

    # собираем все строки ёлки в список строк
    while current <= total:
        row_nums: list[str] = []
        for _ in range(row_len):
            if current > total:
                break
            row_nums.append(str(current))
            current += 1
        lines.append(" ".join(row_nums))
        row_len += 1

    # ширина последней строки — самая большая
    width: int = len(lines[-1])
    # печатаем центрированные строки
    for line in lines:
        print(f"{line:^{width}}")


task_18()


# +
# 19
def task_19() -> None:
    """Task 19: строит матрёшку из чисел."""
    n_num: int = int(input())
    # максимальный слой — в центре, его число равно (n+1)//2
    max_layer: int = (n_num + 1) // 2
    # ширина столбца — длина представления этого числа
    width: int = len(str(max_layer))
    layer: int
    i_num: int
    j_num: int

    for i_num in range(1, n_num + 1):
        for j_num in range(1, n_num + 1):
            # уровень — расстояние до ближайшей границы + 1
            layer = min(i_num, j_num, n_num - i_num + 1, n_num - j_num + 1)
            # выравниваем по правому краю в поле ширины width
            if j_num < n_num:
                print(f"{layer:>{width}}", end=" ")
            else:
                print(f"{layer:>{width}}", end="")
        print()


task_19()


# +
# 20
def task_20() -> None:
    """Task 20: находит основание от 2 до 10, где максимальная сумма цифр."""
    n_num: int = int(input().strip())
    best_base: int = 2
    best_sum: int = -1

    # проверяем каждое основание от 2 до 10
    for base in range(2, 11):
        temp: int = n_num
        digit_sum: int = 0

        # вычисляем сумму цифр в текущем основании
        while temp > 0:
            digit_sum += temp % base
            temp //= base

        # обновляем лучший результат (при равенстве оставляем меньшее
        # основание)
        if digit_sum > best_sum:
            best_sum = digit_sum
            best_base = base

    print(best_base)


task_20()
