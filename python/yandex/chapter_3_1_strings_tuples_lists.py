"""Strings, tuples and lists in python."""

# +
from math import factorial


def task_1() -> None:
    """If our word starts with one of these letters."""
    word: str
    num_of_words: int = int(input())
    for i in range(num_of_words):
        word = input()
        if word[0] == "а" or word[0] == "б" or word[0] == "в":
            if i == num_of_words - 1:
                print("YES")
            continue
        print("NO")
        break


task_1()


# +
def task_2() -> None:
    """Format horizontal string to vertical."""
    horizontal_string: str = input()
    for letter in horizontal_string:
        print(letter)


task_2()


# +
def task_3() -> None:
    """Format titles using slices."""
    requirement_length: int = int(input())
    count_of_titles: int = int(input())
    title: str

    for _ in range(count_of_titles):
        title = input()
        if len(title) <= requirement_length:
            print(title)
        else:
            print(title[: requirement_length - 3], end="...\n")


task_3()


# +
def task_4() -> None:
    """Clear logs."""
    incorrect_string: str

    while (incorrect_string := input()) != "":
        if incorrect_string.startswith("##"):
            incorrect_string = incorrect_string[2:]
        if incorrect_string.endswith("@@@"):
            incorrect_string = ""
        if incorrect_string != "":
            print(incorrect_string)


task_4()


# +
def task_5() -> None:
    """Is it palindrom or not."""
    palindrom_word: str = input()

    if palindrom_word == palindrom_word[::-1]:
        print("YES")
    else:
        print("NO")


task_5()


# +
def task_6() -> None:
    """Count of hares in places."""
    num_of_places: int = int(input())
    count_of_hare: int = 0

    for _ in range(num_of_places):
        place = input()
        count_of_hare += place.count("зайка")
    print(count_of_hare)


task_6()


# +
def task_7() -> None:
    """Split string by spaces and summarize it."""
    string_of_numbers: str = input()
    first, second = string_of_numbers.split()
    print(int(first) + int(second))


task_7()


# +
def task_8() -> None:
    """Get index of word 'зайка' in string place."""
    num_of_places: int = int(input())
    place: str
    for _ in range(num_of_places):
        place = input()
        index_of_hare = place.find("зайка")
        if index_of_hare == -1:
            print("Заек нет =(")
        else:
            print(index_of_hare + 1)


task_8()


# +
def task_9() -> None:
    """Delete '#' symbols from code."""
    string_of_code: str
    index: int

    while (string_of_code := input()) != "":
        if string_of_code.startswith("#"):
            continue
        if (index := string_of_code.find("#")) != -1:
            print(string_of_code[:index].rstrip())
        else:
            print(string_of_code)


task_9()


# +
def task_10() -> None:
    """Print the most frequent letter in lowercase."""
    letters: list[str] = []
    counts: list[int] = []
    line: str

    # Считываем строки до 'ФИНИШ'
    while (line := input()) != "ФИНИШ":
        for ch in line:
            # Пропускаем все, кроме букв
            if not ch.isalpha():
                continue
            lower_ch = ch.lower()
            if lower_ch in letters:
                idx = letters.index(lower_ch)
                counts[idx] += 1
            else:
                letters.append(lower_ch)
                counts.append(1)

    if not letters:
        return

    # Определяем самую частую букву (при равенстве — первая по алфавиту)
    winner = letters[0]
    max_count = counts[0]
    for letter, count in zip(letters, counts):
        if count > max_count or (count == max_count and letter < winner):
            winner = letter
            max_count = count

    print(winner)


task_10()


# +
def task_11() -> None:
    """Print page titles containing the search query."""
    n1: int = int(input())
    titles: list[str] = []
    for _ in range(n1):
        titles.append(input())

    query: str = input().lower()

    for title in titles:
        if query in title.lower():
            print(title)


task_11()


# +
def task_12() -> None:
    """Print which porridge is served for the next N days."""
    n2: int = int(input())
    dishes: list[str] = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]

    for day in range(n2):
        today: str = dishes[day % len(dishes)]
        print(today)


task_12()


# +
def task_13() -> None:
    """Powers number using lists."""
    numbers_count: int = int(input())
    numbers_before_powering: list[int] = []
    for _ in range(numbers_count):
        numbers_before_powering.append(int(input()))
    power: int = int(input())
    for index_of_number in range(numbers_count):
        print(numbers_before_powering[index_of_number] ** power)


task_13()


# +
def task_14() -> None:
    """Raise each number from the input sequence to the specified power."""
    parts: list[str] = input().split()
    numbers: list[int] = [int(x) for x in parts]
    power: int = int(input())
    results: list[int] = []

    for n3 in numbers:
        results.append(n3**power)

    print(*results)


task_14()


# +
def task_15() -> None:
    """Compute the GCD of all numbers given in one line."""
    parts: list[str] = input().split()
    numbers: list[int] = [int(x) for x in parts]

    def gcd(a4: int, b4: int) -> int:
        while b4:
            a4, b4 = b4, a4 % b4
        return a4

    # Инициализируем результат первым числом
    result: int = numbers[0]
    for num in numbers[1:]:
        result = gcd(result, num)

    print(result)


task_15()


# +
def task_16() -> None:
    """Truncate a multi‑line headline."""
    l5: int = int(input())
    n5: int = int(input())
    lines: list[str] = [input() for _ in range(n5)]

    # compute cumulative lengths of lines
    prefix: list[int] = []
    total: int = 0
    for line in lines:
        total += len(line)
        prefix.append(total)

    # case 1: everything fits
    if prefix[-1] <= l5:
        for line in lines:
            print(line)
        return

    # find how many full lines fit
    full: int = 0
    while full < n5 and prefix[full] <= l5:
        full += 1

    # how many chars remaining on the next line
    prev_total: int = prefix[full - 1] if full > 0 else 0
    remain: int = l5 - prev_total

    # keep all fully fitting lines
    result: list[str] = lines[:full]

    if remain <= 3:
        # not enough room for any chars + '...', so
        # append '...' to the last kept line (stripping trailing punctuation
        # first)
        if result:
            result[-1] = result[-1].rstrip(" ,.!?;:") + "..."
        else:
            # edge case: no full lines fit
            result = ["..."]
    else:
        # take exactly remain-3 chars from the next line, then add '...'
        snippet: str = lines[full][: remain - 3]
        result.append(snippet + "...")

    # output the truncated headline
    for line in result:
        print(line)


task_16()


# +
def task_17() -> None:
    """Check if the input string is a palindrome."""
    s6: str = input()
    # Убираем пробелы и приводим к нижнему регистру
    cleaned: str = "".join(ch.lower() for ch in s6 if ch != " ")
    # Сравниваем со строкой в обратном порядке
    if cleaned == cleaned[::-1]:
        print("YES")
    else:
        print("NO")


task_17()


# +
def task_18() -> None:
    """Print each digit and its run length."""
    text: str = input()
    # Use a sentinel that won't appear in the digit string
    text = text + "_"
    reference: str = text[0]
    count: int = 1

    for digit in text[1:]:
        if digit == reference:
            count += 1
        else:
            print(reference, count)
            reference = digit
            count = 1


task_18()


# +
def task_19() -> None:
    """Evaluate an expression in Reverse Polish Notation."""
    tokens: list[str] = input().split()
    stack: list[int] = []

    for token in tokens:
        if token in {"+", "-", "*"}:
            # Pop the two most recent operands
            b7: int = stack.pop()
            a7: int = stack.pop()
            if token == "+":
                stack.append(a7 + b7)
            elif token == "-":
                stack.append(a7 - b7)
            else:  # token == "*"
                stack.append(a7 * b7)
        else:
            # It's a number
            stack.append(int(token))

    # The final result is the only item left on the stack
    print(stack[0])


task_19()


# +
def task_20() -> None:
    """Enhanced RPN calculator."""
    tokens: list[str] = input().split()
    stack: list[int] = []

    for token in tokens:
        if token == "+":
            right_operand = stack.pop()
            left_operand = stack.pop()
            stack.append(left_operand + right_operand)
            continue

        if token == "-":
            right_operand = stack.pop()
            left_operand = stack.pop()
            stack.append(left_operand - right_operand)
            continue

        if token == "*":
            right_operand = stack.pop()
            left_operand = stack.pop()
            stack.append(left_operand * right_operand)
            continue

        if token == "/":
            right_operand = stack.pop()
            left_operand = stack.pop()
            stack.append(left_operand // right_operand)
            continue

        if token == "~":
            operand = stack.pop()
            stack.append(-operand)
            continue

        if token == "!":
            operand = stack.pop()
            stack.append(factorial(operand))
            continue

        if token == "#":
            duplicate_value = stack.pop()
            stack.append(duplicate_value)
            stack.append(duplicate_value)
            continue

        if token == "@":
            third_value = stack.pop()
            second_value = stack.pop()
            first_value = stack.pop()
            stack.append(second_value)
            stack.append(third_value)
            stack.append(first_value)
            continue

        # Integer literal
        stack.append(int(token))

    print(stack[0])


task_20()
