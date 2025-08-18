"""Working with recursion, decorators and generators."""

from collections.abc import Iterator

# +
from types import FunctionType
from typing import Callable, Optional, ParamSpec, TypeVar


def recursive_sum(*positional_args: int) -> int:
    """Return the sum of all positional integer arguments recursively."""
    if not positional_args:
        return 0
    return recursive_sum(*positional_args[:-1]) + positional_args[-1]


# -


def recursive_digit_sum(number: int) -> int:
    """Return the sum of digits of a non-negative integer."""
    if not number:
        return 0
    return recursive_digit_sum(number // 10) + number % 10


def make_equation(*coefficients: int) -> str:
    """Build Horner-form expression string from given coefficients."""
    if len(coefficients) == 1:
        return f"{coefficients[0]}"
    previous_expression: str = make_equation(*coefficients[:-1])
    return f"({previous_expression}) * x + {coefficients[-1]}"


def answer(function: FunctionType) -> object:
    """Добавляет префикс к строковому представлению результата."""

    def new_function(*args: object, **kwargs: object) -> str:
        """Возвращает 'Результат функции: <значение>'."""
        result = function(*args, **kwargs)
        return f"Результат функции: {result}"

    return new_function


def result_accumulator(function: FunctionType) -> object:
    """Копит результаты и отдаёт их списком при method='drop'."""
    results: list[object] = []

    def new_function(*args: object, method: str = "accumulate") -> list[object] | None:
        """Добавляет результат; при 'drop' возвращает накопленное и очищает."""
        result: object = function(*args)
        results.append(result)
        if method == "drop":
            accumulated: list[object] = list(results)
            results.clear()
            return accumulated
        return None

    return new_function


# +
def merge(left: list[int], right: list[int]) -> list[int]:
    """Return a merged sorted list from two sorted input lists."""
    result: list[int] = []
    left_index: int = 0
    right_index: int = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    if left_index < len(left):
        result.extend(left[left_index:])
    if right_index < len(right):
        result.extend(right[right_index:])
    return result


def merge_sort(items: list[int]) -> list[int]:
    """Return the list sorted in ascending order using merge sort."""
    if len(items) <= 1:
        return items.copy()
    middle: int = len(items) // 2
    left_sorted: list[int] = merge_sort(items[:middle])
    right_sorted: list[int] = merge_sort(items[middle:])
    return merge(left_sorted, right_sorted)


# +
_P = ParamSpec("_P")
_R = TypeVar("_R")


def same_type(function: Callable[_P, _R]) -> Callable[_P, Optional[_R]]:
    """Ensure all positional args share the same type."""

    def new_func(*args: _P.args, **kwargs: _P.kwargs) -> Optional[_R]:
        """Return result or None if positional arg types differ."""
        if len(args) > 1 and len(set(map(type, args))) > 1:
            print("Обнаружены различные типы данных")
            return None
        return function(*args, **kwargs)

    return new_func


# -


def fibonacci(count: int) -> Iterator[int]:
    """Yield the first 'count' Fibonacci numbers starting from 0."""
    a1: int = 0
    b1: int = 1
    for _ in range(count):
        yield a1
        a1, b1 = b1, a1 + b1


# +
_Item = TypeVar("_Item")


def cycle(items: list[_Item]) -> Iterator[_Item]:
    """Yield list elements in an infinite repeating sequence."""
    if not items:
        return
    while True:
        yield from items


# -


def make_linear(items: list[object]) -> list[object]:
    """Return a flattened list from a nested list of lists."""
    result: list[object] = []
    for element in items:
        if isinstance(element, list):
            result.extend(make_linear(element))
        else:
            result.append(element)
    return result
