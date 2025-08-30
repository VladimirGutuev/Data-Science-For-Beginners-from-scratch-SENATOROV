"""Working with try, except, else, finally and modules in python."""

# +
import hashlib
import math
import re
import string
from collections.abc import Iterable
from numbers import Real
from typing import TYPE_CHECKING, Callable, Protocol, TypeGuard, cast

if TYPE_CHECKING:

    def func() -> None:
        """Platform-provided function: no params, no return."""


def task_1() -> None:
    """Call provided func and print exception name or 'No Exceptions'."""
    try:
        func()
        print("No Exceptions")
    except (ValueError, TypeError, SystemError) as error:
        print(error.__class__.__name__)


task_1()


# +
def task_2() -> None:
    """Trigger an error inside func using invalid operands."""
    func_ref: object = globals()["func"]
    two_arg_func = cast(Callable[[object, object], object], func_ref)
    two_arg_func(None, None)


task_2()


# +
class BadValue:
    """Object that raises on string or repr conversion."""

    def __str__(self) -> str:
        """Raise TypeError on str()."""
        raise TypeError("string conversion disabled")

    def __repr__(self) -> str:
        """Raise TypeError on repr()."""
        raise TypeError("repr conversion disabled")


def task_3() -> None:
    """Trigger an error inside func via type conversion."""
    bad_value = BadValue()
    func_ref: object = globals()["func"]
    three_arg_func = cast(
        Callable[[object, object, object], object],
        func_ref,
    )
    three_arg_func(bad_value, bad_value, bad_value)


task_3()


# +
def _is_positive_even(number: int) -> bool:
    """Return True if number is a positive even integer."""
    return number > 0 and number % 2 == 0


def only_positive_even_sum(first_value: int, second_value: int) -> int:
    """Return sum of two positive even ints or raise typed errors."""
    are_ints: bool = isinstance(first_value, int) and isinstance(second_value, int)
    if not are_ints:
        raise TypeError
    are_positive_even: bool = _is_positive_even(first_value) and _is_positive_even(
        second_value
    )
    if not are_positive_even:
        raise ValueError
    return first_value + second_value


# +
class Ordered(Protocol):
    """Protocol for values supporting the <= operator."""

    def __le__(self, other: "Ordered") -> bool:
        """Return True if self is less than or equal to other."""


def _is_iterable(value: object) -> TypeGuard[Iterable[object]]:
    """Return True if value is iterable."""
    return isinstance(value, Iterable)


def _ensure_iterable(data: object) -> tuple[object, ...]:
    """Return data as tuple or raise StopIteration if not iterable."""
    if not _is_iterable(data):
        raise StopIteration
    return tuple(data)


def _is_homogeneous(
    values_left: tuple[object, ...],
    values_right: tuple[object, ...],
) -> bool:
    """Return True if all element types across both are the same."""
    left_types = {type(item) for item in values_left}
    right_types = {type(item) for item in values_right}
    return len(left_types | right_types) <= 1


def _is_non_decreasing(values: tuple[Ordered, ...]) -> bool:
    """Return True if sequence is sorted in non-decreasing order."""
    return all(values[i] <= values[i + 1] for i in range(len(values) - 1))


def merge(left: object, right: object) -> tuple[object, ...]:
    """Merge two sorted iterables with validations."""
    left_seq = _ensure_iterable(left)
    right_seq = _ensure_iterable(right)

    if not _is_homogeneous(left_seq, right_seq):
        raise TypeError

    left_ord = cast(tuple[Ordered, ...], left_seq)
    right_ord = cast(tuple[Ordered, ...], right_seq)
    if not (_is_non_decreasing(left_ord) and _is_non_decreasing(right_ord)):
        raise ValueError

    result: list[Ordered] = []
    index_left = 0
    index_right = 0
    while index_left < len(left_ord) and index_right < len(right_ord):
        if left_ord[index_left] <= right_ord[index_right]:
            result.append(left_ord[index_left])
            index_left += 1
        else:
            result.append(right_ord[index_right])
            index_right += 1

    if index_left < len(left_ord):
        result.extend(left_ord[index_left:])
    if index_right < len(right_ord):
        result.extend(right_ord[index_right:])
    return tuple(result)


# +
class NoSolutionsError(Exception):
    """Raised when the equation has no real solutions."""


class InfiniteSolutionsError(Exception):
    """Raised when the equation has infinitely many solutions."""


def _is_real_number(value: object) -> bool:
    """Return True if value is a non-bool real number."""
    return isinstance(value, Real) and not isinstance(value, bool)


def _validate_coefficients(
    coefficient_a: object,
    coefficient_b: object,
    coefficient_c: object,
) -> None:
    """Raise TypeError if any coefficient is not a real number."""
    are_valid = all(
        (
            _is_real_number(coefficient_a),
            _is_real_number(coefficient_b),
            _is_real_number(coefficient_c),
        )
    )
    if not are_valid:
        raise TypeError


def find_roots(
    coefficient_a: Real,
    coefficient_b: Real,
    coefficient_c: Real,
) -> tuple[float, float]:
    """Return two roots for ax^2+bx+c or raise custom errors."""
    _validate_coefficients(coefficient_a, coefficient_b, coefficient_c)

    if coefficient_a == 0:
        if coefficient_b == 0:
            if coefficient_c == 0:
                raise InfiniteSolutionsError
            raise NoSolutionsError
        single_root = -float(coefficient_c) / float(coefficient_b)
        return single_root, single_root

    discriminant = float(coefficient_b) * float(coefficient_b) - 4.0 * float(
        coefficient_a
    ) * float(coefficient_c)
    if discriminant < 0.0:
        raise NoSolutionsError

    sqrt_discriminant = math.sqrt(discriminant)
    denominator = 2.0 * float(coefficient_a)
    root_first = (-float(coefficient_b) - sqrt_discriminant) / denominator
    root_second = (-float(coefficient_b) + sqrt_discriminant) / denominator
    return root_first, root_second


# +
class CyrillicError(Exception):
    """Raised when value contains non-Cyrillic characters."""


class CapitalError(Exception):
    """Raised when capitalization rules are violated."""


def name_validation(personal_name: str) -> str:
    """Validate Cyrillic-only name with proper capitalization."""
    if not isinstance(personal_name, str):
        raise TypeError

    if not re.fullmatch(r"[А-Яа-яЁё]+", personal_name):
        raise CyrillicError

    starts_with_capital: bool = personal_name[0].isupper()
    has_inner_capitals: bool = any(char.isupper() for char in personal_name[1:])
    if not starts_with_capital or has_inner_capitals:
        raise CapitalError

    return personal_name


# +
class BadCharacterError(Exception):
    """Raised when username has characters outside [A-Za-z0-9_]."""


class StartsWithDigitError(Exception):
    """Raised when username starts with a digit."""


def username_validation(user_name: str) -> str:
    """Validate username by alphabet and first char rules."""
    if not isinstance(user_name, str):
        raise TypeError

    is_valid_alphabet: bool = bool(re.fullmatch(r"[A-Za-z0-9_]+", user_name))
    if not is_valid_alphabet:
        raise BadCharacterError

    starts_with_digit: bool = user_name[0].isdigit()
    if starts_with_digit:
        raise StartsWithDigitError

    return user_name


# +
def _are_strs(values: tuple[object, ...]) -> TypeGuard[tuple[str, ...]]:
    """Return True if all items are strings."""
    return all(isinstance(item, str) for item in values)


def user_validation(**user_params: object) -> dict[str, str]:
    """Validate last_name, first_name, username and return dict."""
    required_keys = {"last_name", "first_name", "username"}
    if set(user_params.keys()) != required_keys:
        raise KeyError

    values_tuple: tuple[object, object, object] = (
        user_params["last_name"],
        user_params["first_name"],
        user_params["username"],
    )
    if not _are_strs(values_tuple):
        raise TypeError

    last_name, first_name, username = values_tuple
    valid_last_name: str = name_validation(last_name)
    valid_first_name: str = name_validation(first_name)
    valid_username: str = username_validation(username)

    return {
        "last_name": valid_last_name,
        "first_name": valid_first_name,
        "username": valid_username,
    }


# +
class MinLengthError(Exception):
    """Raised when password length is less than required."""


class PossibleCharError(Exception):
    """Raised when password contains a forbidden character."""


class NeedCharError(Exception):
    """Raised when password lacks a required character."""


DEFAULT_POSSIBLE_CHARS: str = string.ascii_letters + string.digits


def password_validation(
    password_value: str,
    *,
    min_length: int = 8,
    possible_chars: str = DEFAULT_POSSIBLE_CHARS,
    at_least_one: Callable[[str], bool] = str.isdigit,
) -> str:
    """Validate password and return its SHA-256 hex digest."""
    if not isinstance(password_value, str):
        raise TypeError

    if len(password_value) < min_length:
        raise MinLengthError

    invalid_chars = set(password_value) - set(possible_chars)
    if invalid_chars:
        raise PossibleCharError

    has_required: bool = any(map(at_least_one, password_value))
    if not has_required:
        raise NeedCharError

    return hashlib.sha256(password_value.encode()).hexdigest()
