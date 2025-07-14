"""Yandex contest of chapter 2.2 of Python course."""

# 1
name_of_user: str = input("Как Вас зовут?\n")
print("Здравствуйте, ", name_of_user, "!", sep="")
user_happiness: str = input("Как дела?\n")
if user_happiness == "хорошо":
    print("Я за Вас рада!")
else:
    print("Всё наладится!")

# +
# 2
first_cyclist_speed_for_race: float = float(input()) * 1000
second_cyclist_speed_for_race: float = float(input()) * 1000

if 43872 / first_cyclist_speed_for_race < 43872 / second_cyclist_speed_for_race:
    print("Петя")
else:
    print("Вася")

# +
# 3
DISTANCE_M: float = 43_872.0  # фиксированная дистанция, м

first_cyclist_speed: float = float(input()) * 1_000  # м/ч
second_cyclist_speed: float = float(input()) * 1_000
third_cyclist_speed: float = float(input()) * 1_000

first_time: float = DISTANCE_M / first_cyclist_speed
second_time: float = DISTANCE_M / second_cyclist_speed
third_time: float = DISTANCE_M / third_cyclist_speed

if first_time < second_time and first_time < third_time:
    print("Петя")
elif second_time < third_time:
    print("Вася")
else:
    print("Толя")

# +
# 4
distance: int = 43872

speed_petya: float = float(input())
speed_vasya: float = float(input())
speed_tolya: float = float(input())

time_petya: float = distance / speed_petya
time_vasya: float = distance / speed_vasya
time_tolya: float = distance / speed_tolya

# Определяем первое место
if time_petya <= time_vasya and time_petya <= time_tolya:
    first: str = "Петя"
    # между Васей и Толей — второе/третье
    if time_vasya <= time_tolya:
        second: str = "Вася"
        third: str = "Толя"
    else:
        second = "Толя"
        third = "Вася"

elif time_vasya <= time_petya and time_vasya <= time_tolya:
    first = "Вася"
    if time_petya <= time_tolya:
        second = "Петя"
        third = "Толя"
    else:
        second = "Толя"
        third = "Петя"

else:
    first = "Толя"
    if time_petya <= time_vasya:
        second = "Петя"
        third = "Вася"
    else:
        second = "Вася"
        third = "Петя"

print(f"1. {first}")
print(f"2. {second}")
print(f"3. {third}")

# +
# 5
petya_apples: int = 6
vasya_apples: int = 9

apples_to_petya: int = int(input())
apples_to_vasya: int = int(input())

petya_apples += apples_to_petya
vasya_apples += apples_to_vasya

if petya_apples > vasya_apples:
    print("Петя")
else:
    print("Вася")

# +
# 6
year: int = int(input())

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("YES")
else:
    print("NO")

# +
# 7
DIGITS_IN_NUMBER: int = 4  # константа длины, чтобы не использовать «магию»

input_number: int = int(input())  # исходное число
number_text: str = f"{input_number:0{DIGITS_IN_NUMBER}d}"  # строка из 4 цифр

if number_text == number_text[::-1]:  # сравниваем с обратной
    print("YES")
else:
    print("NO")
# -

# 8
phrase: str = input()
if "зайка" in phrase:
    print("YES")
else:
    print("NO")

# +
# 9
name1: str = input()
name2: str = input()
name3: str = input()

# Предположим, что первый кандидат — name1
first_candidate: str = name1

if name2 < first:
    first_candidate = name2

if name3 < first:
    first_candidate = name3

# Выводим, кто "меньший" по алфавиту
print(first_candidate)

# +
# 10
all_numb: str = input()

number_first: int = int(all_numb) // 100
number_second: int = int(all_numb) // 10 % 10
number_third: int = int(all_numb) % 10

sec_and_third_sum = int(f"{number_second + number_third}")
first_and_sec_sum = int(f"{number_first + number_second}")

if first_and_sec_sum < sec_and_third_sum:
    print(f"{sec_and_third_sum}" + f"{first_and_sec_sum}")
else:
    print(f"{first_and_sec_sum}" + f"{sec_and_third_sum}")

# +
# 11
# Считываем трёхзначное число
n_num: int = int(input())

d1: int = n_num // 100
d2: int = (n_num // 10) % 10
d3: int = n_num % 10

# Находим минимум и максимум через условные выражения
min_d: int = d1 if d1 <= d2 and d1 <= d3 else (d2 if d2 <= d3 else d3)
max_d: int = d1 if d1 >= d2 and d1 >= d3 else (d2 if d2 >= d3 else d3)

mid_d: int = d1 + d2 + d3 - min_d - max_d

if min_d + max_d == mid_d * 2:
    print("YES")
else:
    print("NO")

# +
# 12
first_side: int = int(input())
second_side: int = int(input())
third_side: int = int(input())

# сортируем, чтобы самый длинный отрезок был последним
sides: list[int] = sorted((first_side, second_side, third_side))

if sides[0] + sides[1] < sides[2]:
    print("YES")  # неравенство треугольника нарушено
else:
    print("NO")  # треугольник возможен

# +
# 13
first_num: str = input().zfill(2)  # страхуемся, если ввели «5» вместо «05»
second_num: str = input().zfill(2)
third_num: str = input().zfill(2)

if first_num[0] == second_num[0] == third_num[0]:  # разряд десятков
    print(first_num[0])
else:  # значит, совпали единицы
    print(first_num[1])

# +
three_digit_number: int = int(input())

# ── извлекаем цифры
hundreds_digit: int = three_digit_number // 100
tens_digit: int = (three_digit_number // 10) % 10
units_digit: int = three_digit_number % 10

# ── все шесть возможных комбинаций (ab, ac, ba, bc, ca, cb)
candidate_numbers: list[int] = [
    hundreds_digit * 10 + tens_digit,
    hundreds_digit * 10 + units_digit,
    tens_digit * 10 + hundreds_digit,
    tens_digit * 10 + units_digit,
    units_digit * 10 + hundreds_digit,
    units_digit * 10 + tens_digit,
]

# ── отсекаем «однозначные» варианты (старший разряд = 0)
two_digit_numbers: list[int] = [num for num in candidate_numbers if num >= 10]

# ── ищем минимальное и максимальное без лишних if-блоков
minimal_number: int = min(two_digit_numbers)
maximal_number: int = max(two_digit_numbers)

print(minimal_number, maximal_number)

# +
first_number: int = int(input())
second_number: int = int(input())

# Разбираем оба числа на отдельные цифры
digits: list[int] = [
    first_number // 10,
    first_number % 10,
    second_number // 10,
    second_number % 10,
]

max_digit: int = max(digits)
min_digit: int = min(digits)

# «Средняя» — единицы суммы двух оставшихся цифр
middle_digit: int = (sum(digits) - max_digit - min_digit) % 10

# Выводим трёхзначное магическое число слитно
print(f"{max_digit}{middle_digit}{min_digit}")

# +
# 16
# Считываем скорости претендентов
petya_speed: int = int(input())
vasya_speed: int = int(input())
tolya_speed: int = int(input())

# Определяем максимальную и минимальную скорость
winner_speed: int = max(petya_speed, vasya_speed, tolya_speed)
loser_speed: int = min(petya_speed, vasya_speed, tolya_speed)

# Объявляем переменные для имён
winner: str
second_cyclist: str
loser: str

# Логика определения первого, второго и третьего места
if winner_speed == petya_speed:
    winner = "Петя"
    if loser_speed == tolya_speed:
        loser, second_cyclist = "Толя", "Вася"
    else:
        loser, second_cyclist = "Вася", "Толя"
elif winner_speed == tolya_speed:
    winner = "Толя"
    if loser_speed == petya_speed:
        loser, second_cyclist = "Петя", "Вася"
    else:
        loser, second_cyclist = "Вася", "Петя"
else:
    winner = "Вася"
    if loser_speed == tolya_speed:
        loser, second_cyclist = "Толя", "Петя"
    else:
        loser, second_cyclist = "Петя", "Толя"

# Ширина ступени пьедестала
step_width: int = 8

# Печатаем "красивый пьедестал"
print(f'{"": ^{step_width}}{winner: ^{step_width}}{"": ^{step_width}}')
print(f'{second_cyclist: ^{step_width}}{"": ^{step_width}}{"": ^{step_width}}')
print(f'{"": ^{step_width}}{"": ^{step_width}}{loser: ^{step_width}}')
print(f'{"II": ^{step_width}}{"I": ^{step_width}}{"III": ^{step_width}}')

# +
# 17
eps: float = 1e-12

a_num: float = float(input())
b_num: float = float(input())
c_num: float = float(input())

# Квадратное уравнение
if abs(a_num) > eps:
    discriminant: float = b_num * b_num - 4 * a_num * c_num

    if discriminant > eps:
        sqrt_disc: float = discriminant**0.5
        x1: float = (-b_num - sqrt_disc) / (2 * a_num)
        x2: float = (-b_num + sqrt_disc) / (2 * a_num)
        # Два корня в порядке возрастания
        if x1 <= x2:
            print(f"{x1:.2f} {x2:.2f}")
        else:
            print(f"{x2:.2f} {x1:.2f}")

    elif abs(discriminant) <= eps:
        x_num: float = -b_num / (2 * a_num)
        print(f"{x_num:.2f}")

    else:
        print("No solution")

# Линейное уравнение bx + c = 0
elif abs(b_num) > eps:
    x_num = -c_num / b_num
    print(f"{x_num:.2f}")

# 0·x + c = 0
elif abs(c_num) <= eps:
    print("Infinite solutions")

else:
    print("No solution")

# +
# 18
tolerance: float = 1e-12

# Считываем длины сторон треугольника
first_side_length: float = float(input())
second_side_length: float = float(input())
third_side_length: float = float(input())

# Определяем самую длинную сторону и две остальные
if first_side_length >= second_side_length and first_side_length >= third_side_length:
    longest_side_length: float = first_side_length
    other_side_length1: float = second_side_length
    other_side_length2: float = third_side_length
elif (
    second_side_length >= first_side_length and second_side_length >= third_side_length
):
    longest_side_length = second_side_length
    other_side_length1 = first_side_length
    other_side_length2 = third_side_length
else:
    longest_side_length = third_side_length
    other_side_length1 = first_side_length
    other_side_length2 = second_side_length

# Вычисляем квадраты длин
sum_of_smaller_squares: float = (
    other_side_length1 * other_side_length1 + other_side_length2 * other_side_length2
)
square_of_longest: float = longest_side_length * longest_side_length

# Классификация треугольника по форме
if abs(sum_of_smaller_squares - square_of_longest) <= tolerance:
    # Если прямой
    print("100%")
elif sum_of_smaller_squares > square_of_longest:
    # Если остроугольный
    print("крайне мала")
else:
    # Если тупоугольный
    print("велика")

# +
# 19
# координаты исследователя
x_coord: float = float(input())
y_coord: float = float(input())

# константы
ISLAND_RADIUS_SQ: float = 100.0  # 10² — проверяем без извлечения корня


def is_inside_island(x_value: float, y_value: float) -> bool:
    """Точка лежит в круге радиуса 10 (остров)."""
    return x_value * x_value + y_value * y_value <= ISLAND_RADIUS_SQ


def lower_parabola_y(x_value: float) -> float:
    """Y-координата нижней границы зыбучих песков.

    парабола: y = (9/35)·x² + (18/35)·x − 9.
    """
    return (9.0 / 35.0) * x_value * x_value + (18.0 / 35.0) * x_value - 9.0


def is_inside_quicksand(x_value: float, y_value: float) -> bool:
    """Точка лежит в зоне зыбучих песков."""
    # Ниже параболы уже безопасно
    if y_value < lower_parabola_y(x_value):
        return False

    # Левый сегмент (x ≤ –4)
    if x_value <= -4.0:
        return 2.0 * x_value + 14.0 <= y_value <= 6.0

    # Верхний горизонтальный сегмент (–4 < x < 1)
    if -4.0 < x_value < 1.0:
        return y_value <= 6.0

    # Правый сегмент (1 ≤ x ≤ 5)
    if x_value <= 5.0:
        return y_value <= -1.5 * x_value + 7.5

    # Правее 5 — вне зыбучих песков
    return False


# вывод результата
if not is_inside_island(x_coord, y_coord):
    print("Вы вышли в море и рискуете быть съеденным акулой!")
elif is_inside_quicksand(x_coord, y_coord):
    print("Опасность! Покиньте зону как можно скорее!")
else:
    print("Зона безопасна. Продолжайте работу.")

# +
# 20
# чтение исходных описаний
first_description: str = input()
second_description: str = input()
third_description: str = input()

# ищем строки, в которых встречается слово «зайка»
matching_descriptions: list[str] = []

for current_description in (
    first_description,
    second_description,
    third_description,
):
    if "зайка" in current_description:
        matching_descriptions.append(current_description)

# среди подходящих выбираем лексикографически минимальную
chosen_description: str = min(matching_descriptions)

# длина выбранной строки
description_length: int = len(chosen_description)

# вывод результата
print(chosen_description, end=" ")
print(description_length)
