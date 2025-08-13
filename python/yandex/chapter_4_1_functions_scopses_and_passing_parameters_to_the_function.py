"""Working with functions, scopes, passing parameters to the functions."""

# +
from itertools import product


def print_hello(name: str) -> None:
    """Print a greeting: Hello, <name>!."""
    print(f"Hello, {name}!")


# -


def gcd(left: int, right: int) -> int:
    """Return the greatest common divisor of two natural numbers."""
    left = abs(left)
    right = abs(right)
    while right != 0:
        left, right = right, left % right
    return left


def number_length(number: int) -> int:
    """Return the count of digits in an integer, ignoring the sign."""
    return len(str(abs(number)))


def take_small(money: list[float | int]) -> list[float | int]:
    """Return items from money that are less than 100, keeping order."""
    return [amount for amount in money if amount < 100]


# +
# __count: int = 0 !!! В задании требовалось использовать global переменную,
# а линтер не пропускает, поэтому принял решение закомментировать, а так
# задание проходит все линтеры !!!


# def click() -> None:
#     """Increase the click counter by one."""
#     global __count
#     __count += 1


# def get_count() -> int:
#     """Return the current value of the click counter."""
#     return __count

# +
# __total: int = 0 !!! В задании требовалось использовать global переменную, а
# линтер не пропускает, поэтому принял решение закомментировать, а так задание
# проходит все линтеры !!!


# def move(player: str, number: int) -> None:
#     """Update shared total: Petya adds number, Vanya subtracts it."""
#     global __total
#     if player == "Петя":
#         __total += number
#     elif player == "Ваня":
#         __total -= number


# def game_over() -> str:
#     """Return the result: 'Петя', 'Ваня' or 'Ничья'."""
#     if __total > 0:
#         return "Петя"
#     if __total < 0:
#         return "Ваня"
#     return "Ничья"
# -


def max2d(matrix: list[list[int]]) -> int:
    """Return the maximum element in a 2D list of integers."""
    return max(max(row) for row in matrix)


def fragments(numbers: list[int]) -> list[list[int]]:
    """Split a list into strictly increasing contiguous fragments."""
    if not numbers:
        return []
    parts: list[list[int]] = [[numbers[0]]]
    previous: int = numbers[0]
    for value in numbers[1:]:
        if value > previous:
            parts[-1].append(value)
        else:
            parts.append([value])
        previous = value
    return parts


# +
MONTH_NAMES: dict[str, tuple[str, ...]] = {
    "ru": (
        "Январь",
        "Февраль",
        "Март",
        "Апрель",
        "Май",
        "Июнь",
        "Июль",
        "Август",
        "Сентябрь",
        "Октябрь",
        "Ноябрь",
        "Декабрь",
    ),
    "en": (
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ),
}


def month(number: int, language: str) -> str:
    """Return month name by number and language ('ru' or 'en')."""
    return MONTH_NAMES[language][number - 1]


# -


def split_numbers(text: str) -> tuple[int, ...]:
    """Return a tuple of integers from a space-separated string."""
    return tuple(int(chunk) for chunk in text.split())


def find_mountains(heights: list[int]) -> tuple[int, ...]:
    """Return 1-based indices of elements higher than both neighbours."""
    return tuple(
        idx
        for idx, (left, middle, right) in enumerate(
            zip(heights, heights[1:], heights[2:]), 2
        )
        if middle > left and middle > right
    )


def find_mountains2(
    data: list[list[int | float]],
) -> tuple[tuple[int, int], ...]:
    """Return 1-based coordinates of cells higher than all 8 neighbours."""
    rows: int = len(data)
    cols: int = len(data[0]) if rows else 0
    if rows < 3 or cols < 3:
        return ()
    peaks: list[tuple[int, int]] = []
    for i1, j1 in product(range(1, rows - 1), range(1, cols - 1)):
        value = data[i1][j1]
        if all(
            value > data[r1][c1]
            for r1, c1 in product(range(i1 - 1, i1 + 2), range(j1 - 1, j1 + 2))
            if (r1, c1) != (i1, j1)
        ):
            peaks.append((i1 + 1, j1 + 1))
    return tuple(peaks)


# +
__printed_lines: set[str] = set()


def modern_print(text: str) -> None:
    """Print text only if it hasn't been printed before."""
    if text not in __printed_lines:
        print(text)
        __printed_lines.add(text)


# -


def can_eat(horse: tuple[int, int], other: tuple[int, int]) -> bool:
    """Return True if a knight at `horse` can capture a piece at `other`."""
    (hx, hy), (ox, oy) = horse, other
    dx: int = abs(hx - ox)
    dy: int = abs(hy - oy)
    return dx * dy == 2


def get_dict(text: str) -> dict[str, int | float | str]:
    """Parse 'k=v;...' into a dict, casting values to int/float."""

    def to_number(value: str) -> int | float | str:
        value = value.strip()
        unsigned = value.lstrip("-")
        if unsigned.isdigit():
            return int(value)
        if value.count(".") == 1:
            core = value[1:] if value.startswith("-") else value
            left, right = core.split(".", 1)
            if left.isdigit() and right.isdigit():
                return float(value)
        return value

    result: dict[str, int | float | str] = {}
    for item in text.split(";"):
        if not item:
            continue
        key, raw_value = item.split("=", 1)
        result[key] = to_number(raw_value)
    return result


def is_palindrome(
    value: int | str | list[object] | tuple[object, ...],
) -> bool:
    """Return True if value reads the same forwards and backwards."""
    if isinstance(value, int):
        text: str = str(value)
        return text == text[::-1]
    return value == value[::-1]


def is_prime(number: int) -> bool:
    """Return True if the given natural number is prime."""
    if number < 2:
        return False
    if number % 2 == 0:
        return number == 2
    divisor: int = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True


def merge(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    """Merge two ascending tuples of ints into one ascending tuple."""
    left_index: int = 0
    right_index: int = 0
    merged: list[int] = []

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    if left_index < len(left):
        merged.extend(left[left_index:])
    if right_index < len(right):
        merged.extend(right[right_index:])
    return tuple(merged)


def swap(left: list[object], right: list[object]) -> None:
    """Swap the contents of two lists in place, preserving identities."""
    backup: list[object] = left[:]
    left[:] = right
    right[:] = backup


# +
ROMAN_DIGITS: list[tuple[int, str]] = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]


def to_roman(number: int) -> str:
    """Convert a positive integer to a Roman numeral."""
    pieces: list[str] = []
    for value, symbol in ROMAN_DIGITS:
        while number >= value:
            pieces.append(symbol)
            number -= value
    return "".join(pieces)


def roman(left: int, right: int) -> str:
    """Return 'ROMAN_LEFT + ROMAN_RIGHT = ROMAN_SUM'."""
    left_r: str = to_roman(left)
    right_r: str = to_roman(right)
    total_r: str = to_roman(left + right)
    return f"{left_r} + {right_r} = {total_r}"
