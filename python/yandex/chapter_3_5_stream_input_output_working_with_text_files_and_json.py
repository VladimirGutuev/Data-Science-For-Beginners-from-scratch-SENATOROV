"""Working with input and output stream, with text files and json."""

# +
import json
import math
import os
from collections.abc import Iterator
from sys import stdin
from typing import TypedDict


def task_1() -> None:
    """Sum all numbers in input stream."""
    summary: int = 0
    for line in stdin:
        line = line.strip("\n")
        summary += sum(map(int, line.split()))
    print(summary)


task_1()


# +
def task_2() -> None:
    """Print rounded change of average height in class."""
    previous_heights: list[int] = []
    current_heights: list[int] = []

    for line in stdin:
        parts: list[str] = line.split()
        if len(parts) != 3:
            continue
        _, prev_str, curr_str = parts
        previous_heights.append(int(prev_str))
        current_heights.append(int(curr_str))

    if not previous_heights:
        print(0)
        return

    previous_avg: float = sum(previous_heights) / len(previous_heights)
    current_avg: float = sum(current_heights) / len(current_heights)
    change_avg: float = current_avg - previous_avg

    print(round(change_avg))


task_2()


# +
def task_3() -> None:
    """Print program lines without comments."""
    for source_line in stdin:
        line: str = source_line.rstrip("\n")
        if line.lstrip().startswith("#"):
            continue

        in_single: bool = False
        in_double: bool = False
        escaped: bool = False
        result_chars: list[str] = []

        for ch in line:
            if ch == "\\" and not escaped:
                result_chars.append(ch)
                escaped = True
                continue

            if not escaped and ch == "'" and not in_double:
                in_single = not in_single
            elif not escaped and ch == '"' and not in_single:
                in_double = not in_double
            elif ch == "#" and not in_single and not in_double:
                break

            result_chars.append(ch)
            escaped = False

        cleaned: str = "".join(result_chars)
        print(cleaned)


task_3()


# +
def task_4() -> None:
    """Print page titles containing the query (case-insensitive)."""
    lines: list[str] = [ln.rstrip("\n") for ln in stdin]
    if not lines:
        return

    query: str = lines[-1]
    titles: list[str] = lines[:-1]
    normalized_query: str = query.casefold()

    for title in titles:
        if normalized_query in title.casefold():
            print(title)


task_4()


# +
def task_5() -> None:
    """Print unique palindromic words sorted alphabetically."""
    result: set[str] = set()

    for line in stdin:
        for word in line.split():
            normalized: str = word.casefold()
            if normalized == normalized[::-1]:
                result.add(word)

    for word in sorted(result):
        print(word)


task_5()


# +
def task_6() -> None:
    """Transliterate cyrillic.txt to transliteration.txt per rules."""
    lower_map: dict[str, str] = {
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
    upper_map: dict[str, str] = {
        "А": "A",
        "Б": "B",
        "В": "V",
        "Г": "G",
        "Д": "D",
        "Е": "E",
        "Ё": "E",
        "Ж": "Zh",
        "З": "Z",
        "И": "I",
        "Й": "I",
        "К": "K",
        "Л": "L",
        "М": "M",
        "Н": "N",
        "О": "O",
        "П": "P",
        "Р": "R",
        "С": "S",
        "Т": "T",
        "У": "U",
        "Ф": "F",
        "Х": "Kh",
        "Ц": "Tc",
        "Ч": "Ch",
        "Ш": "Sh",
        "Щ": "Shch",
        "Ы": "Y",
        "Э": "E",
        "Ю": "Iu",
        "Я": "Ia",
        "Ъ": "",
        "Ь": "",
    }

    with open("cyrillic.txt", encoding="utf-8") as src:
        text: str = src.read()

    out_parts: list[str] = []
    for ch in text:
        if ch in lower_map:
            out_parts.append(lower_map[ch])
        elif ch in upper_map:
            out_parts.append(upper_map[ch])
        else:
            out_parts.append(ch)

    with open("transliteration.txt", "w", encoding="utf-8") as dst:
        dst.write("".join(out_parts))


task_6()


# +
def task_7() -> None:
    """Print basic stats for numbers in a file."""
    filename: str = input()

    with open(filename, encoding="utf-8") as src:
        numbers: list[int] = [int(token) for token in src.read().split()]

    count_all: int = len(numbers)
    count_positive: int = sum(1 for value in numbers if value > 0)
    min_value: int = min(numbers)
    max_value: int = max(numbers)
    total_sum: int = sum(numbers)
    average: float = total_sum / count_all

    print(count_all)
    print(count_positive)
    print(min_value)
    print(max_value)
    print(total_sum)
    print(f"{average:.2f}")


task_7()


# +
def task_8() -> None:
    """Write unique words from two files into third file, sorted."""
    first_filename: str = input()
    second_filename: str = input()
    output_filename: str = input()

    with open(first_filename, encoding="utf-8") as first_file:
        words_first: set[str] = set(first_file.read().split())

    with open(second_filename, encoding="utf-8") as second_file:
        words_second: set[str] = set(second_file.read().split())

    only_in_one: list[str] = sorted(words_first ^ words_second)

    with open(output_filename, "w", encoding="utf-8") as out_file:
        out_file.write("\n".join(only_in_one))


task_8()


# +
def task_9() -> None:
    """Clean text using only str.replace (tabs, spaces, newlines)."""
    source_name: str = input()
    output_name: str = input()

    with open(source_name, encoding="utf-8") as src:
        text: str = src.read()

    # удаляем табы
    text = text.replace("\t", "")

    # схлопываем повторяющиеся пробелы
    while "  " in text:
        text = text.replace("  ", " ")

    # убираем пробелы в начале/конце каждой строки
    while "\n " in text or " \n" in text or text.startswith(" ") or text.endswith(" "):
        text = text.replace("\n ", "\n")
        text = text.replace(" \n", "\n")
        if text.startswith(" "):
            text = text[1:]
        if text.endswith(" "):
            text = text[:-1]

    # схлопываем повторяющиеся переводы строки
    while "\n\n" in text:
        text = text.replace("\n\n", "\n")

    with open(output_name, "w", encoding="utf-8") as dst:
        dst.write(text)


task_9()


# +
def task_10() -> None:
    """Print the last N lines of a file (tail)."""
    filename: str = input()
    lines_to_show: int = int(input())

    block_size: int = 4096
    chunks: list[bytes] = []
    newline_count: int = 0

    with open(filename, "rb") as fh:
        fh.seek(0, 2)  # в конец файла
        pos: int = fh.tell()

        while pos > 0 and newline_count <= lines_to_show:
            read_size: int = block_size if pos >= block_size else pos
            pos -= read_size
            fh.seek(pos)
            chunk: bytes = fh.read(read_size)
            chunks.append(chunk)
            newline_count += chunk.count(b"\n")

    data: bytes = b"".join(reversed(chunks)).rstrip(b"\n")
    if not data or lines_to_show <= 0:
        return

    lines: list[bytes] = data.split(b"\n")
    tail_lines: list[bytes] = lines[-lines_to_show:]

    for raw in tail_lines:
        print(raw.decode("utf-8"))


task_10()


# +
def task_11() -> None:
    """Save basic stats of numbers from a file to JSON."""
    source_name: str = input()
    output_name: str = input()

    with open(source_name, encoding="utf-8") as src:
        numbers: list[int] = [int(tok) for tok in src.read().split()]

    count_all: int = len(numbers)
    positive_count: int = sum(1 for v in numbers if v > 0)
    min_value: int = min(numbers)
    max_value: int = max(numbers)
    total_sum: int = sum(numbers)
    average: float = round(total_sum / count_all, 2)

    stats: dict[str, int | float] = {
        "count": count_all,
        "positive_count": positive_count,
        "min": min_value,
        "max": max_value,
        "sum": total_sum,
        "average": average,
    }

    with open(output_name, "w", encoding="utf-8") as out:
        json.dump(stats, out, indent=4, ensure_ascii=False)


task_11()


# +
def task_12() -> None:
    """Split numbers by digit parity domination into three files."""
    source_name: str = input()
    out_names: list[str] = [input(), input(), input()]
    out_lines: list[list[str]] = [[], [], []]

    with open(source_name, encoding="utf-8") as src_file:
        for line in src_file:
            parts: list[str] = line.split()
            per_bucket: list[list[str]] = [[], [], []]

            for token in parts:
                digits: str = token.lstrip("+-")
                even_count: int = sum(ch in "02468" for ch in digits)
                twice_even: int = even_count * 2
                if twice_even > len(digits):
                    bucket_index: int = 0
                elif twice_even < len(digits):
                    bucket_index = 1
                else:
                    bucket_index = 2
                per_bucket[bucket_index].append(token)

            for bucket_index in range(3):
                out_lines[bucket_index].append(" ".join(per_bucket[bucket_index]))

    for bucket_index, name in enumerate(out_names):
        with open(name, "w", encoding="utf-8") as dst:
            dst.write("\n".join(out_lines[bucket_index]) + "\n")


task_12()


# +
def task_13() -> None:
    """Update a JSON file with key == value lines from stdin."""
    filename: str = input()

    with open(filename, encoding="utf-8") as src:
        raw: dict[str, object] = json.load(src)
    data: dict[str, str] = {k: str(v) for k, v in raw.items()}

    for raw_line in stdin:
        if "==" not in raw_line:
            continue
        key_part, value_part = raw_line.split("==", 1)
        key: str = key_part.strip()
        value: str = value_part.strip()
        if key:
            data[key] = value

    with open(filename, "w", encoding="utf-8") as dst:
        json.dump(data, dst, ensure_ascii=False, indent=4)


task_13()

# +


def task_14() -> None:
    """Merge users and updates into name-keyed JSON with max values."""
    users_filename: str = input()
    updates_filename: str = input()

    users_map: dict[str, dict[str, str]] = {}

    # Загружаем исходных пользователей и сразу раскладываем в словарь
    with open(users_filename, encoding="utf-8") as src:
        for rec in json.load(src):
            user_name: str = str(rec.get("name", ""))
            if not user_name:
                continue
            users_map[user_name] = {
                key: str(val) for key, val in rec.items() if key != "name"
            }

    # Применяем обновления: при конфликте берём лексикографически большее
    with open(updates_filename, encoding="utf-8") as src:
        for rec in json.load(src):
            upd_name: str = str(rec.get("name", ""))
            if not upd_name:
                continue
            upd_fields: dict[str, str] = {
                key: str(val) for key, val in rec.items() if key != "name"
            }
            current: dict[str, str] = users_map.get(upd_name, {})
            for field, new_val in upd_fields.items():
                current[field] = (
                    new_val if field not in current else max(current[field], new_val)
                )
            users_map[upd_name] = current

    with open(users_filename, "w", encoding="utf-8") as dst:
        json.dump(users_map, dst, ensure_ascii=False, indent=4)


task_14()


# +
class Test(TypedDict):
    """Class 1."""

    inputt: str
    pattern: str


class Group(TypedDict):
    """Class 2."""

    points: int
    tests: list[Test]


def task_15() -> None:
    """Compute score from stdin answers using scoring.json spec."""
    with open("scoring.json", encoding="utf-8") as src:
        groups: list[Group] = json.load(src)

    answers: Iterator[str] = (line.strip() for line in stdin)
    total_points: int = 0

    for group in groups:
        points: int = int(group["points"])
        tests: list[Test] = group["tests"]
        per_test: int = points // len(tests)
        passed: int = 0

        for test in tests:
            expected: str = test["pattern"]
            actual: str = next(answers, "")
            if actual == expected:
                passed += 1

        total_points += per_test * passed

    print(total_points)


task_15()


# +
def normalize(text: str) -> str:
    """Lowercase and collapse all whitespace into single spaces."""
    return " ".join(text.casefold().split())


def task_16() -> None:
    """Print files where query occurs ignoring case and whitespace."""
    query_raw: str = input()
    filenames: list[str] = [name.rstrip("\n") for name in stdin]

    query_norm: str = normalize(query_raw)
    matched: list[str] = []

    for filename in filenames:
        with open(filename, encoding="utf-8") as src:
            content_norm: str = normalize(src.read())
        if query_norm in content_norm:
            matched.append(filename)

    if matched:
        print("\n".join(matched))
    else:
        print("404. Not Found")


task_16()


# +
def task_17() -> None:
    """Reveal message by taking the low byte of each character."""
    with open("secret.txt", encoding="utf-8") as src:
        secret_text: str = src.read()

    decoded_chars: list[str] = []
    for symbol in secret_text:
        code_point: int = ord(symbol)
        new_code: int = code_point if code_point < 128 else (code_point & 0xFF)
        decoded_chars.append(chr(new_code))

    print("".join(decoded_chars))


task_17()


# +
def task_18() -> None:
    """Print file size in standard units with ceiling rounding."""
    filename: str = input()
    size_bytes: int = os.path.getsize(filename)

    units: list[tuple[str, int]] = [
        ("Б", 1),
        ("КБ", 1024),
        ("МБ", 1024**2),
        ("ГБ", 1024**3),
    ]

    if size_bytes == 0:
        print("0Б")
        return

    unit_name: str = "Б"
    divisor: int = 1
    for name, factor in units:
        if factor <= size_bytes:
            unit_name, divisor = name, factor

    value: int = math.ceil(size_bytes / divisor)
    print(f"{value}{unit_name}")


task_18()


# +
def task_19() -> None:
    """Encrypt public.txt using Caesar shift for Latin letters only."""
    shift_value: int = int(input())
    offset: int = shift_value % 26

    def shift_letter(symbol: str, offset_val: int) -> str:
        """Shift one Latin letter by offset; keep others unchanged."""
        if "a" <= symbol <= "z":
            base: int = ord("a")
            pos: int = ord(symbol) - base
            return chr(base + (pos + offset_val) % 26)
        if "A" <= symbol <= "Z":
            base = ord("A")
            pos = ord(symbol) - base
            return chr(base + (pos + offset_val) % 26)
        return symbol

    with open("public.txt", encoding="utf-8") as src:
        plain_text: str = src.read()

    cipher_text: str = "".join(shift_letter(ch, offset) for ch in plain_text)

    with open("private.txt", "w", encoding="utf-8") as dst:
        dst.write(cipher_text)


task_19()


# +
def task_20() -> None:
    """Sum 2-byte big-endian numbers from numbers.num with 16-bit wrap."""
    with open("numbers.num", "rb") as src:
        payload: bytes = src.read()

    usable_len: int = len(payload) - (len(payload) % 2)
    total_sum: int = sum(
        int.from_bytes(payload[i : i + 2], "big", signed=False)
        for i in range(0, usable_len, 2)
    )

    print(total_sum % (1 << 16))


task_20()
