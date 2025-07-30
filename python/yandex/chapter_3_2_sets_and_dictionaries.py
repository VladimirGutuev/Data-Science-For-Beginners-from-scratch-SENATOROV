"""Sets and dictionaries in python."""

# +
import json
import math


def task_1() -> None:
    """Print unique letters of word."""
    data: set[str] = set(input())
    print(*data, sep="")


task_1()


# +
def task_2() -> None:
    """Print intersection of words."""
    first_word: set[str] = set(input())
    second_word: set[str] = set(input())
    result_word: set[str] = first_word.intersection(second_word)
    print(*result_word, sep="")


task_2()


# +
def task_3() -> None:
    """Count number of things."""
    count_of_places: int = int(input())
    all_things: set[str] = set()
    for _ in range(count_of_places):
        place: set[str] = set(input().split())
        all_things = all_things | place
    print(*all_things, sep="\n")


task_3()


# +
def task_4() -> None:
    """Count the number of intersections."""
    count_semolina_lovers: int = int(input())
    count_oatmeal_lovers: int = int(input())

    semolina_lovers: set[str] = set()
    for _ in range(count_semolina_lovers):
        student_surname2: str = input().strip()
        semolina_lovers.add(student_surname2)

    oatmeal_lovers: set[str] = set()
    for _ in range(count_oatmeal_lovers):
        student_surname2 = input().strip()
        oatmeal_lovers.add(student_surname2)

    both_lovers: set[str] = semolina_lovers & oatmeal_lovers

    if both_lovers:
        print(len(both_lovers))
    else:
        print("Таких нет")


task_4()


# +
def task_5() -> None:
    """Count children who like exactly one porridge."""
    count_semolina_lovers: int = int(input())
    count_oatmeal_lovers: int = int(input())
    total_entries: int = count_semolina_lovers + count_oatmeal_lovers

    surname_counts: dict[str, int] = {}
    for _ in range(total_entries):
        surname: str = input()
        surname_counts[surname] = surname_counts.get(surname, 0) + 1

    only_one_count: int = sum(
        1 for occurrences in surname_counts.values() if occurrences == 1
    )
    if only_one_count:
        print(only_one_count)
    else:
        print("Таких нет")


task_5()


# +
def task_6() -> None:
    """List children who like exactly one porridge."""
    count_semolina_lovers: int = int(input())
    count_oatmeal_lovers: int = int(input())
    total_entries: int = count_semolina_lovers + count_oatmeal_lovers

    surname_counts: dict[str, int] = {}
    for _ in range(total_entries):
        surname: str = input()
        surname_counts[surname] = surname_counts.get(surname, 0) + 1

    unique_lovers: list[str] = [
        name for name, occurrences in surname_counts.items() if occurrences == 1
    ]
    if unique_lovers:
        unique_lovers.sort()
        for name in unique_lovers:
            print(name)
    else:
        print("Таких нет")


task_6()


# +
def task_7() -> None:
    """Encode each word of input text into Morse code."""
    morse: dict[str, str] = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
    }
    words: list[str] = input().split()
    for word in words:
        encoded_letters: list[str] = [morse[char.upper()] for char in word]
        print(" ".join(encoded_letters))


task_7()


# +
def task_8() -> None:
    """List surnames of children who like a given porridge."""
    count_children: int = int(input())
    food_to_names: dict[str, list[str]] = {}
    for _ in range(count_children):
        name, *foods = input().split()
        for food in foods:
            if food not in food_to_names:
                food_to_names[food] = [name]
            else:
                food_to_names[food].append(name)
    query: str = input()
    result: list[str] = food_to_names.get(query, [])
    if result:
        for surname in sorted(result):
            print(surname)
    else:
        print("Таких нет")


task_8()


# +
def task_9() -> None:
    """Count occurrences of each word."""
    counts: dict[str, int] = {}
    while True:
        line: str = input()
        if line == "":
            break
        for word in line.split():
            counts[word] = counts.get(word, 0) + 1
    for word, count in counts.items():
        print(word, count)


task_9()


# +
def task_10() -> None:
    """Transliterate Russian text to Latin per standard R 52535.1-2006."""
    mapping_lower: dict[str, str] = {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ё": "e",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "й": "i",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "kh",
        "ц": "tc",
        "ч": "ch",
        "ш": "sh",
        "щ": "shch",
        "ы": "y",
        "э": "e",
        "ю": "iu",
        "я": "ia",
        "ъ": "",
        "ь": "",
    }
    text: str = input()
    result: list[str] = []
    for ch in text:
        lower_char: str = ch.lower()
        if lower_char in mapping_lower:
            latin: str = mapping_lower[lower_char]
            if latin:
                result.append(latin.capitalize() if ch.isupper() else latin)
        else:
            result.append(ch)
    print("".join(result))


task_10()


# +
def task_11() -> None:
    """Count employees with duplicate surnames."""
    count_employees: int = int(input())
    surname_counts: dict[str, int] = {}
    for _ in range(count_employees):
        surname: str = input()
        surname_counts[surname] = surname_counts.get(surname, 0) + 1
    duplicate_total: int = sum(cnt for cnt in surname_counts.values() if cnt > 1)
    print(duplicate_total)


task_11()


# +
def task_12() -> None:
    """List duplicate surnames with their counts."""
    count_employees: int = int(input())
    surname_counts: dict[str, int] = {}
    for _ in range(count_employees):
        surname: str = input()
        surname_counts[surname] = surname_counts.get(surname, 0) + 1

    duplicates: list[tuple[str, int]] = [
        (name, cnt) for name, cnt in surname_counts.items() if cnt > 1
    ]

    if not duplicates:
        print("Однофамильцев нет")
    else:
        for name, cnt in sorted(duplicates, key=lambda item: item[0]):
            print(f"{name} - {cnt}")


task_12()


# +
def task_13() -> None:
    """List dishes not cooked this week."""
    count_dishes: int = int(input())
    all_dishes: set[str] = set()
    for _ in range(count_dishes):
        dish: str = input()
        all_dishes.add(dish)

    count_days: int = int(input())
    cooked: set[str] = set()
    for _ in range(count_days):
        dishes_today: int = int(input())
        for _ in range(dishes_today):
            dish = input()
            cooked.add(dish)

    to_cook: set[str] = all_dishes - cooked
    if to_cook:
        for dish in sorted(to_cook):
            print(dish)
    else:
        print("Готовить нечего")


task_13()


# +
def task_14() -> None:
    """Determine which recipes can be cooked given available products."""
    count_products: int = int(input())
    available_products: set[str] = {input() for _ in range(count_products)}

    count_recipes: int = int(input())
    cookable: list[str] = []
    for _ in range(count_recipes):
        dish_name: str = input()
        num_ingredients: int = int(input())
        required: set[str] = {input() for _ in range(num_ingredients)}
        if required <= available_products:
            cookable.append(dish_name)

    if cookable:
        for name in sorted(cookable):
            print(name)
    else:
        print("Готовить нечего")


task_14()


# +
def task_15() -> None:
    """Compute binary digit, one‑count and zero‑count statistics."""
    tokens: list[str] = input().split()
    result: list[dict[str, int]] = []
    for tok in tokens:
        number: int = int(tok)
        binary: str = f"{number:b}"
        result.append(
            {
                "digits": len(binary),
                "units": binary.count("1"),
                "zeros": binary.count("0"),
            }
        )
    print(json.dumps(result, ensure_ascii=False, indent=4))


task_15()


# +
def task_16() -> None:
    """Find objects adjacent to the word 'зайка' in the descriptions."""
    neighbors: set[str] = set()
    while True:
        line: str = input()
        if line == "":
            break
        words: list[str] = line.split()
        for idx, word in enumerate(words):
            if word == "зайка":
                if idx > 0:
                    neighbors.add(words[idx - 1])
                if idx < len(words) - 1:
                    neighbors.add(words[idx + 1])
    for obj in neighbors:
        print(obj)


task_16()


# +
def task_17() -> None:
    """Compute second‑level friends for each person."""
    # build adjacency: each person maps to a set of direct friends
    friend_map: dict[str, set[str]] = {}
    while True:
        line: str = input()
        if not line:
            break
        person1, person2 = line.split()
        for p1, q1 in ((person1, person2), (person2, person1)):
            if p1 not in friend_map:
                friend_map[p1] = set()
            friend_map[p1].add(q1)

    # for each person in alphabetical order, compute friends of friends
    for person in sorted(friend_map):
        second_level: set[str] = set()
        for direct in friend_map[person]:
            # add all friends of this direct friend
            second_level |= friend_map.get(direct, set())
        # exclude the person themself and their direct friends
        second_level.discard(person)
        second_level -= friend_map[person]

        if second_level:
            print(f"{person}: {', '.join(sorted(second_level))}")
        else:
            # nobody at second level
            print(f"{person}:")


task_17()


# +
def task_18() -> None:
    """Compute the maximum number of points."""
    count_points: int = int(input())
    freq: dict[tuple[int, int], int] = {}
    for _ in range(count_points):
        x_coord, y_coord = map(int, input().split())
        key = (x_coord // 10, y_coord // 10)
        freq[key] = freq.get(key, 0) + 1

    print(max(freq.values(), default=0))


task_18()


# +
def task_19() -> None:
    """Read N children with their toys."""
    count_children: int = int(input())
    toy_owner_counts: dict[str, int] = {}

    for _ in range(count_children):
        line: str = input()
        # split into name and the comma‑separated list of toys
        _, toys_part = line.split(":", 1)
        # collect each toy once per child
        owned: set[str] = set()
        for raw_toy in toys_part.split(","):
            toy_name: str = raw_toy.strip()
            if toy_name:
                owned.add(toy_name)
        # increment the owner count for each toy
        for toy in owned:
            toy_owner_counts[toy] = toy_owner_counts.get(toy, 0) + 1

    # select those toys owned by exactly one child
    unique_toys: list[str] = [
        toy for toy, owners in toy_owner_counts.items() if owners == 1
    ]

    # output in alphabetical order
    for toy in sorted(unique_toys):
        print(toy)


task_19()


# +
def task_20() -> None:
    """For each number, list other numbers that are coprime with it."""
    # read numbers separated by ';' and optional spaces
    tokens: list[str] = [tok.strip() for tok in input().split(";") if tok.strip()]
    numbers: list[int] = [int(tok) for tok in tokens]

    # work with each unique number in ascending order
    unique_numbers: list[int] = sorted(set(numbers))

    for a2 in unique_numbers:
        # find others b2 ≠ a2 with gcd(a2, b2) == 1
        coprimes: list[int] = [
            b2 for b2 in unique_numbers if b2 != a2 and math.gcd(a2, b2) == 1
        ]
        if coprimes:
            # format: "a - b1, b2, b3, ..."
            print(f"{a2} - {', '.join(str(b2) for b2 in coprimes)}")


task_20()
