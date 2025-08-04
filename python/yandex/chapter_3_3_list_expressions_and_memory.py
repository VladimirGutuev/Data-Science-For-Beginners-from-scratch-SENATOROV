"""List Expressions: Memory Model for Python Types."""

# +
from collections.abc import Sequence


def task_1() -> None:
    """Square numbers."""
    a_num: int = 1
    b_num: int = 5
    numbers_squared: list[int] = [i_num**2 for i_num in range(a_num, b_num + 1)]
    print(numbers_squared)


task_1()


# +
def task_2() -> None:
    """Square numbers also wise versa."""
    a_num: int = 6
    b_num: int = -3
    numbers_squared2: list[int] = [
        x_num**2
        for x_num in range(
            a_num, b_num + (1 if a_num < b_num else -1), 1 if a_num < b_num else -1
        )
    ]
    print(numbers_squared2)


task_2()


# +
def task_3() -> None:
    """Make list only with numbers from a to b multiples of d."""
    a_num: int = 1
    b_num: int = 5
    d_num: int = 2
    numbers_filtered: list[int] = [
        i_num for i_num in range(a_num, b_num + 1) if i_num % d_num == 0
    ]
    print(numbers_filtered)


task_3()


# +
def task_4() -> None:
    """Make set only with even numbers."""
    numbers: list[int] = [1, 2, 3, 4, 5]
    numbers_filtered: set[int] = {i_num for i_num in numbers if i_num % 2 != 0}
    print(numbers_filtered)


task_4()


# +
def task_5() -> None:
    """Make set only with fully squared nums."""
    numbers: list[int] = [1, 2, 3, 4, 5]
    numbers_filtered: set[int] = {
        i_num for i_num in numbers if i_num == int(i_num**0.5) ** 2
    }
    print(numbers_filtered)


task_5()


# +
def task_6() -> None:
    """Make list length of words in sentence."""
    sentence: str = "Ехали медведи на велосипеде"
    numbers_filtered: list[int] = [
        len(i_num) for i_num in sentence.split() if i_num != " "
    ]
    print(numbers_filtered)


task_6()


# +
def task_7() -> None:
    """Extract all digits from the given text and print as a single string."""
    text: str = (
        "33 коровы,\n"
        "33 коровы,\n"
        "33 коровы -\n"
        "Свежая строка.\n"
        "33 коровы,\n"
        "Стих родился новый,\n"
        "Как стакан парного молока.\n"
        "Стих родился новый,\n"
        "Как стакан парного молока.\n"
    )
    digits_list: list[str] = [character for character in text if character.isdigit()]
    digits_string: str = "".join(digits_list)
    print(digits_string)


task_7()


# +
def task_8() -> None:
    """Generate an abbreviation from the first letters words in the string."""
    string: str = "Российская Федерация"
    abbreviation: str = "".join([word[0].upper() for word in string.split()])
    print(abbreviation)


task_8()


# +
def task_9() -> None:
    """Convert a list of natural numbers."""
    numbers: list[int] = [3, 1, 2, 3, 2, 2, 1]
    unique_sorted: list[int] = sorted(set(numbers))
    stringified_numbers: list[str] = [str(value) for value in unique_sorted]
    result: str = " - ".join(stringified_numbers)
    print(result)


task_9()


# +
def task_10() -> None:
    """Filter words containing three or more vowels."""
    words: str = "Ехали медведи на велосипеде"
    result: list[str] = [
        word
        for word in words.split()
        if sum(letter.lower() in "ауоэеиыaeiouy" for letter in word) >= 3
    ]
    print(result)


task_10()


# +
def task_11() -> None:
    """Build set of numbers occurring exactly once in the list."""
    numbers: list[int] = [1, 2, 1, 3, 1, 2, 2, 4, 5]
    unique_once: set[int] = {value for value in numbers if numbers.count(value) == 1}
    print(unique_once)


task_11()


# +
def task_12() -> None:
    """Return max product of two different numbers from the set."""
    numbers: set[int] = {1, 2, 3, 4, 5}
    max_product: int = max(
        first * second for first in numbers for second in numbers if first != second
    )
    print(max_product)


task_12()


# +
def task_13() -> None:
    """Find the key whose list values sum to the smallest total."""
    data: dict[str, list[int]] = {"a": [1, 2, 3], "b": [2, 3, 4, 5]}
    result: str = min((sum(values), key) for key, values in data.items())[1]
    print(result)


task_13()


# +
def task_14() -> None:
    """Build set of keys whose lists contain duplicates."""
    data: dict[str, list[int]] = {"a": [1, 2, 1], "b": [2, 3, 2, 5, 1]}
    repeated_keys: set[str] = {
        key for key, values in data.items() if len(values) != len(set(values))
    }
    print(repeated_keys)


task_14()


# +
def task_15() -> None:
    """Count letter frequencies in the given text."""
    text: str = "Мама мыла раму!"
    frequencies: dict[str, int] = {
        letter.lower(): text.lower().count(letter.lower())
        for letter in text
        if letter.isalpha()
    }
    print(frequencies)


task_15()


# +
def task_16() -> None:
    """Restore string from run-length encoding list."""
    rle: list[tuple[str, int]] = [("a", 2), ("b", 3), ("c", 1)]
    result: str = "".join(letter * count for letter, count in rle)
    print(result)


task_16()


# +
def task_17() -> None:
    """Generate multiplication table of size n_num."""
    n_num: int = 3
    table: list[list[int]] = [
        [row * col for col in range(1, n_num + 1)] for row in range(1, n_num + 1)
    ]
    print(table)


task_17()


# +
def task_18() -> None:
    """Map each number to its divisors (1 through the number)."""
    numbers: set[int] = {1, 2, 3, 4, 5}
    divisors_map: dict[int, list[int]] = {
        num: [i for i in range(1, num + 1) if num % i == 0] for num in numbers
    }
    print(divisors_map)


task_18()


# +
def task_19() -> None:
    """Filter prime numbers from the given set."""
    numbers: set[int] = {1, 2, 3, 4, 5}
    primes: set[int] = {
        number
        for number in numbers
        if number > 1 and all(number % divisor for divisor in range(2, number))
    }
    print(primes)


task_19()


# +
def task_20() -> None:
    """Find word pairs with ≥3 common letters."""
    text: str = "ехали медведи на велосипеде"
    words_list: Sequence[str] = text.split()
    common_pairs: set[tuple[str, str]] = {
        (first, second)
        for first in words_list
        for second in words_list
        if first < second and len(set(first) & set(second)) >= 3
    }
    print(common_pairs)


task_20()
