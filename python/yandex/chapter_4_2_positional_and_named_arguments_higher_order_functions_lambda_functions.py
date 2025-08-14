"""Positional and named arguments, higher-order and lambda functions."""

# +
from __future__ import annotations

import re
from datetime import date, datetime
from operator import add, eq, floordiv, ge, gt, le, lt, mul, ne
from operator import pow as op_pow
from operator import sub
from typing import Callable, Final, Literal, ParamSpec, TypeVar


def make_list(length: int, value: object = 0) -> list[object]:
    """Return a list of the given length filled with the provided value."""
    return [value for _index in range(length)]


# -


def make_matrix(
    size: int | tuple[int, int],
    value: object = 0,
) -> list[list[object]]:
    """Create a matrix of given size filled with value."""
    if isinstance(size, tuple):
        matrix_width, matrix_height = size
    else:
        matrix_width = matrix_height = size

    return [[value for _ in range(matrix_width)] for _ in range(matrix_height)]


def gcd(*numbers: int) -> int:
    """Return the greatest common divisor of given natural numbers."""
    current: int = abs(numbers[0])
    for value in numbers[1:]:
        a1: int = current
        b1: int = abs(value)
        while b1 != 0:
            a1, b1 = b1, a1 % b1
        current = a1
        if current == 1:
            break
    return current


def month(number: int, language: Literal["ru", "en"] = "ru") -> str:
    """Return the month name by number in the chosen language."""
    months_by_lang: dict[str, tuple[str, ...]] = {
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
    return months_by_lang[language][number - 1]


def to_string(*data: object, sep: str = " ", end: str = "\n") -> str:
    """Return values joined by sep with end appended."""
    return sep.join(str(value) for value in data) + end


# +
OpSym = Literal["+", "-", "*", "//", "**"]
BinaryOp = Callable[[int, int], int]


def get_operator(symbol: OpSym) -> BinaryOp:
    """Return a two-arg int operator matching the symbol."""
    operators: dict[OpSym, BinaryOp] = {
        "+": add,
        "-": sub,
        "*": mul,
        "//": floordiv,
        "**": op_pow,
    }
    return operators[symbol]


# +
Params = ParamSpec("Params")


def get_formatter(sep: str = " ", end: str = "") -> Callable[Params, str]:
    """Return a function that joins args with sep and appends end."""

    def formatter(*args: Params.args, **_kwargs: Params.kwargs) -> str:
        """Format arbitrary values using captured sep and end."""
        return sep.join(str(value) for value in args) + end

    return formatter


# -


def grow(*positional: int, **named: int) -> tuple[int, ...]:
    """Increase positional ints by kwargs, divisibility checks the original."""
    result: list[int] = list(positional)
    for name, add_value in named.items():
        name_len: int = len(name)
        for index, original in enumerate(positional):
            if original % name_len == 0:
                result[index] += add_value
    return tuple(result)


def product(*strings: str, **factors: int) -> tuple[int, ...]:
    """Return products of kwargs whose keys occur in each given string."""
    results: list[int] = []
    for text in strings:
        value_product: int = 1
        matched: bool = False
        for key, factor in factors.items():
            if key in text:
                value_product *= factor
                matched = True
        if matched:
            results.append(value_product)
    return tuple(results)


def choice(
    *numbers: int,
    **mode: Callable[[int], int],
) -> int:
    """Apply function from kwarg to args and return min or max of results."""
    if "min" in mode:
        transform = mode["min"]
        pick_minimum = True
    else:
        transform = mode["max"]
        pick_minimum = False

    best_value: int = transform(numbers[0])
    for number in numbers[1:]:
        current: int = transform(number)
        if (pick_minimum and current < best_value) or (
            not pick_minimum and current > best_value
        ):
            best_value = current
    return best_value


# +
DrinkName = Literal[
    "Эспрессо",
    "Капучино",
    "Макиато",
    "Кофе по-венски",
    "Латте Макиато",
    "Кон Панна",
]

RECIPES: dict[DrinkName, dict[str, int]] = {
    "Эспрессо": {"coffee": 1},
    "Капучино": {"coffee": 1, "milk": 3},
    "Макиато": {"coffee": 2, "milk": 1},
    "Кофе по-венски": {"coffee": 1, "cream": 2},
    "Латте Макиато": {"coffee": 1, "milk": 2, "cream": 1},
    "Кон Панна": {"coffee": 1, "cream": 1},
}

# На платформе переопределят актуальными запасами.
in_stock: dict[str, int] = {}

APOLOGY: str = "К сожалению, не можем предложить Вам напиток"


def order(*preferences: DrinkName) -> str:
    """Return first makeable drink and update stock or apology."""
    for drink in preferences:
        recipe = RECIPES.get(drink)
        if recipe is None:
            continue

        enough: bool = True
        for ingredient, amount in recipe.items():
            if in_stock.get(ingredient, 0) < amount:
                enough = False
                break

        if enough:
            for ingredient, amount in recipe.items():
                in_stock[ingredient] -= amount
            return drink

    return APOLOGY


# +
# Глобальное хранилище пар результатов (x, y)
DATA: list[tuple[float, float]] = []

ZERO_PAIR: Final[tuple[float, float]] = (0.0, 0.0)


def enter_results(*values: float) -> None:
    """Store results as pairs (x, y)."""
    for left, right in zip(values[::2], values[1::2]):
        DATA.append((float(left), float(right)))


def _as_num(value: float) -> float:
    """Round to 2 decimals; return int when it is an exact integer."""
    rounded: float = round(value, 2)
    return int(rounded) if rounded.is_integer() else rounded


def get_sum() -> tuple[float, float]:
    """Return pair of sums rounded to hundredths (0.0, 0.0 if empty)."""
    if not DATA:
        return ZERO_PAIR
    sx: float = sum(x for x, _ in DATA)
    sy: float = sum(y for _, y in DATA)
    return _as_num(sx), _as_num(sy)


def get_average() -> tuple[float, float]:
    """Return pair of averages rounded to hundredths (0.0, 0.0 if empty)."""
    if not DATA:
        return ZERO_PAIR
    sx, sy = get_sum()
    n1: int = len(DATA)
    return _as_num(float(sx) / n1), _as_num(float(sy) / n1)


# +
# Закомментировал т.к. линтер не принимает не назначенные лямбда функции,
# однако яндекс контест требует именно такой формат
# lambda word: (len(word), word.lower())

# +
# Закомментировал т.к. линтер не принимает не назначенные лямбда функции,
# однако яндекс контест требует именно такой формат
# lambda number: sum(map(int, str(number))) % 2 == 0

# +
T = TypeVar("T")


def get_repeater(func: Callable[[T], T], count: int) -> Callable[[T], T]:
    """Return a function applying func to a value count times."""

    def repeater(value: T) -> T:
        result: T = value
        for _ in range(count):
            result = func(result)
        return result

    return repeater


# +
Callback = Callable[[str], None]


def login(
    username: str,
    password: str,
    success: Callback,
    error: Callback,
) -> None:
    """Check password and call success or error with the username."""
    codes_sum: int = sum(ord(char) for char in username)
    expected_hex: str = f"{codes_sum * len(username):x}"
    if expected_hex == password[::-1].lower():
        success(username)
    else:
        error(username)


# +
# Закомментировал т.к. линтер не принимает не назначенные лямбда функции,
# однако яндекс контест требует именно такой формат
# lambda kv: isinstance(kv[1], list) and any(
#     isinstance(x, int) and x % 2 == 0 for x in kv[1]
# )

# +
# Закомментировал т.к. линтер не принимает не назначенные лямбда функции,
# однако яндекс контест требует именно такой формат
# lambda kv: (
#     "".join(c for c in kv[0].lower() if c.isalpha()),
#     (
#         sum(kv[1])
#         if (hasattr(kv[1], "__iter__") and not isinstance(kv[1], str))
#         else kv[1]
#     ),
# )
# -


def secret_replace(text: str, **rules: tuple[str, ...]) -> str:
    """Return text after cyclic, ordered replacements per rules."""
    for key, variants in rules.items():
        idx: int = 0
        position: int = 0
        key_len: int = len(key)
        parts: list[str] = []
        while position < len(text):
            is_match: bool = text.startswith(key, position)
            if is_match:
                parts.append(variants[idx])
                idx = (idx + 1) % len(variants)
                position += key_len
            else:
                parts.append(text[position])
                position += 1
        text = "".join(parts)
    return text


# +
# Тип записи пользователя и хранилище
User = dict[str, int | str]
USERS: list[User] = []

# Операции сравнения
Comparable = int | str | date
OPS: dict[str, Callable[[Comparable, Comparable], bool]] = {
    "==": eq,
    "!=": ne,
    "<": lt,
    "<=": le,
    ">": gt,
    ">=": ge,
}


def insert(*users: User) -> None:
    """Insert one or more users; enforce unique id and name."""
    for user in users:
        new_id: int = int(user["id"])
        new_name: str = str(user["name"])
        new_birth: str = str(user["birth"])

        index: int = 0
        while index < len(USERS):
            existing_user = USERS[index]
            if existing_user["id"] == new_id or existing_user["name"] == new_name:
                USERS.pop(index)
            else:
                index += 1

        USERS.append({"id": new_id, "name": new_name, "birth": new_birth})


def _parse_condition(expr: str) -> tuple[str, str, str]:
    """Parse '<field> <op> <value>' into parts."""
    match = re.match(
        r"^\s*(id|name|birth)\s*(==|!=|<=|>=|<|>)\s*(.+?)\s*$",
        expr,
    )
    if match is None:
        raise ValueError("Invalid condition")
    return match.group(1), match.group(2), match.group(3)


def _as_date(text: str) -> date:
    """Convert DD.MM.YYYY to date."""
    return datetime.strptime(text, "%d.%m.%Y").date()


def _is_condition_met(user: User, field: str, op: str, raw: str) -> bool:
    """Return True if user satisfies 'field op raw'."""
    if field == "id":
        left_value: Comparable = int(user["id"])
        right_value: Comparable = int(raw)
    elif field == "birth":
        left_value = _as_date(str(user["birth"]))
        right_value = _as_date(raw)
    else:  # field == "name"
        left_value = str(user["name"])
        right_value = raw

    return OPS[op](left_value, right_value)


def select(*criteria: str) -> list[User]:
    """Return users filtered by criteria (AND), ordered by id."""
    if not criteria:
        return sorted(USERS, key=lambda user_record: int(user_record["id"]))

    parsed = [_parse_condition(cond) for cond in criteria]
    result: list[User] = []
    for user in USERS:
        matches_all: bool = True
        for field, op, raw in parsed:
            if not _is_condition_met(user, field, op, raw):
                matches_all = False
                break
        if matches_all:
            result.append(user)
    result.sort(key=lambda user_record: int(user_record["id"]))
    return result
