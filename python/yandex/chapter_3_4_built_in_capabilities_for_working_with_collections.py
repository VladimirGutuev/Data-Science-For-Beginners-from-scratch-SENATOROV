"""Working with built-in functions from python and itertools."""

# +
import re
from collections.abc import Iterator
from itertools import (
    accumulate,
    chain,
    combinations,
    count,
    cycle,
    islice,
    permutations,
    product,
    zip_longest,
)
from typing import Callable, ClassVar


def task_1() -> None:
    """Numbers words and outputs one by one with index."""
    string: str = input()
    for index, word in enumerate(string.split(), 1):
        print(f"{index}. {word}")


task_1()


# +
def task_2() -> None:
    """Create pairs."""
    first_line: str = input()
    second_line: str = input()
    for first, second in zip(first_line.split(", "), second_line.split(", ")):
        print(first, second, sep=" - ")


task_2()


# +
def task_3() -> None:
    """Infinity iterator."""
    parameters: str = input()
    for x1 in count(float(parameters.split()[0]), float(parameters.split()[2])):
        if x1 >= float(parameters.split()[1]):
            break
        print(round(x1, 2))


task_3()


# +
def task_4() -> None:
    """Print lines with one more accumulated word each time."""
    input_text: str = input()
    words_list: list[str] = input_text.split()
    accumulated_lines: list[str] = list(
        accumulate(words_list, lambda previous, current: f"{previous} {current}")
    )
    for line in accumulated_lines:
        print(line)


task_4()


# +
def task_5() -> None:
    """Collect family wishes into sorted numbered list."""
    raw_inputs: list[str] = [input() for _ in range(3)]
    split_lists: list[list[str]] = [line.split(", ") for line in raw_inputs]
    sorted_items: list[str] = sorted(chain(*split_lists))
    for index, item in enumerate(sorted_items, start=1):
        print(f"{index}. {item}")


task_5()


# +
def task_6() -> None:
    """Generate a deck of cards excluding a specified suit."""
    excluded_suit: str = input()
    all_suits: list[str] = ["пик", "треф", "бубен", "червей"]
    ranks: list[str] = [
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "валет",
        "дама",
        "король",
        "туз",
    ]
    available_suits: list[str] = [s for s in all_suits if s != excluded_suit]
    for rank, suit in product(ranks, available_suits):
        print(f"{rank} {suit}")


task_6()


# +
def task_7() -> None:
    """Generate all possible games in a round-robin tournament."""
    total_players: int = int(input())
    player_names: list[str] = [input() for _ in range(total_players)]
    for first, second in combinations(player_names, 2):
        print(f"{first} - {second}")


task_7()


# +
def task_8() -> None:
    """Generate kasha schedule for the next N days."""
    total_kashes: int = int(input())
    menu: list[str] = [input() for _ in range(total_kashes)]
    days: int = int(input())
    for porridge in islice(cycle(menu), days):
        print(porridge)


task_8()


# +
def task_9() -> None:
    """Generate an N×N multiplication table."""
    size: int = int(input())
    for row_index in range(1, size + 1):
        products: list[str] = [
            str(row_index * col_index) for col_index in range(1, size + 1)
        ]
        print(" ".join(products))


task_9()


# +
def task_10() -> None:
    """Print all ways to split slices among Anya, Borya, and Vova."""
    total_slices: int = int(input())
    # Header with initials (Cyrillic letters)
    print("А Б В")
    for anya_count, borya_count in product(range(1, total_slices), repeat=2):
        vova_count: int = total_slices - anya_count - borya_count
        if vova_count >= 1:
            print(f"{anya_count} {borya_count} {vova_count}")


task_10()


# +
def task_11() -> None:
    """Build numeric rectangle with equal-width columns."""
    height: int = int(input())
    width: int = int(input())
    max_value: int = height * width
    column_width: int = len(str(max_value))
    numbers: list[int] = list(range(1, max_value + 1))
    # create `width` references to the same iterator for chunking
    iterators: list[Iterator[int]] = [iter(numbers)] * width
    for chunk in zip_longest(*iterators, fillvalue=0):
        # each chunk is one row of `width` numbers
        row_cells: list[str] = [str(value).rjust(column_width) for value in chunk]
        print(" ".join(row_cells))


task_11()


# +
def task_12() -> None:
    """Merge family shopping lists and print sorted numbered list."""
    member_count: int = int(input())
    raw_lists: list[list[str]] = [input().split(", ") for _ in range(member_count)]
    sorted_items: list[str] = sorted(chain(*raw_lists))
    for index, item in enumerate(sorted_items, start=1):
        print(f"{index}. {item}")


task_12()


# +
def task_13() -> None:
    """Print all starting arrangements of athletes alphabetically."""
    count2: int = int(input())
    names: list[str] = sorted(input() for _ in range(count2))
    for arrangement in permutations(names):
        print(", ".join(arrangement))


task_13()


# +
def task_14() -> None:
    """Generate all possible podium finishers (top 3) in alphabetical order."""
    total_athletes: int = int(input())
    athletes: list[str] = sorted(input() for _ in range(total_athletes))
    for podium in permutations(athletes, 3):
        print(", ".join(podium))


task_14()


# +
def task_15() -> None:
    """Generate all 3-item shopping list variants alphabetically."""
    member_count: int = int(input())
    raw_lists: list[list[str]] = [input().split(", ") for _ in range(member_count)]
    items: list[str] = sorted(chain(*raw_lists))
    for combo in permutations(items, 3):
        print(" ".join(combo))


task_15()


# +
def task_16() -> None:
    """List first 10 triples with required suit and without forbidden rank."""
    # map nominative input to genitive suit name
    nom_to_gen: dict[str, str] = {
        "буби": "бубен",
        "пики": "пик",
        "трефы": "треф",
        "черви": "червей",
    }
    required_nom: str = input().strip()
    required_suit: str = nom_to_gen[required_nom]
    forbidden_rank: str = input().strip()

    ranks: list[str] = [str(i) for i in range(2, 11)] + [
        "валет",
        "дама",
        "король",
        "туз",
    ]
    suits: list[str] = list(nom_to_gen.values())
    deck: list[str] = sorted(f"{rank} {suit}" for rank in ranks for suit in suits)

    printed: int = 0
    for triple in combinations(deck, 3):
        # must include at least one card of the required suit
        if not any(card.split()[1] == required_suit for card in triple):
            continue
        # must not include any card of the forbidden rank
        if any(card.split()[0] == forbidden_rank for card in triple):
            continue
        print(", ".join(triple))
        printed += 1
        if printed == 10:
            break


task_16()


# +
def task_17() -> None:
    """Find the next valid triple of cards after the given previous variant."""
    # Map from nominative to genitive suit names
    nom_to_gen: dict[str, str] = {
        "буби": "бубен",
        "пики": "пик",
        "трефы": "треф",
        "черви": "червей",
    }
    required_nom: str = input().strip()
    required_suit: str = nom_to_gen[required_nom]
    forbidden_rank: str = input().strip()
    previous_variant: str = input().strip()

    ranks: list[str] = [str(i) for i in range(2, 11)] + [
        "валет",
        "дама",
        "король",
        "туз",
    ]
    suits: list[str] = list(nom_to_gen.values())
    deck: list[str] = sorted(f"{rank} {suit}" for rank in ranks for suit in suits)

    seen_previous: bool = False
    for triple in combinations(deck, 3):
        # must include at least one card of the required suit
        if not any(card.split()[1] == required_suit for card in triple):
            continue
        # must not include any card of the forbidden rank
        if any(card.split()[0] == forbidden_rank for card in triple):
            continue
        triple_str: str = ", ".join(triple)
        if seen_previous:
            print(triple_str)
            break
        if triple_str == previous_variant:
            seen_previous = True


task_17()

# +
PRECEDENCE: dict[str, int] = {"not": 3, "and": 2, "or": 1}
ASSOCIATIVITY: dict[str, str] = {"not": "right", "and": "left", "or": "left"}


def is_operator_pop_required(current_op: str, top_op: str) -> bool:
    """Return True if top operator must be popped before pushing current."""
    is_left: bool = ASSOCIATIVITY[current_op] == "left"
    is_right: bool = ASSOCIATIVITY[current_op] == "right"
    le_prec: bool = PRECEDENCE[current_op] <= PRECEDENCE[top_op]
    lt_prec: bool = PRECEDENCE[current_op] < PRECEDENCE[top_op]
    return (is_left and le_prec) or (is_right and lt_prec)


def to_rpn(tokens: list[str]) -> list[str]:
    """Convert infix tokens to Reverse Polish Notation."""
    output: list[str] = []
    op_stack: list[str] = []
    for token in tokens:
        if token in ("a", "b", "c"):
            output.append(token)
        elif token == "(":
            op_stack.append(token)
        elif token == ")":
            while op_stack and op_stack[-1] != "(":
                output.append(op_stack.pop())
            op_stack.pop()
        else:
            while op_stack and op_stack[-1] != "(":
                top_op: str = op_stack[-1]
                if not is_operator_pop_required(token, top_op):
                    break
                output.append(op_stack.pop())
            op_stack.append(token)
    while op_stack:
        output.append(op_stack.pop())
    return output


def is_rpn_true(postfix_tokens: list[str], environment: dict[str, bool]) -> bool:
    """Evaluate RPN boolean expression for environment."""
    stack: list[bool] = []
    for token in postfix_tokens:
        if token in environment:
            stack.append(environment[token])
        elif token == "not":
            operand: bool = stack.pop()
            stack.append(not operand)
        else:
            right: bool = stack.pop()
            left: bool = stack.pop()
            stack.append(left and right if token == "and" else left or right)
    return stack[0]


def task_18() -> None:
    """Build truth table for expression in a, b, c."""
    expression_text: str = input().strip()
    tokens: list[str] = expression_text.split()
    rpn_tokens: list[str] = to_rpn(tokens)

    print("a b c f")
    for a_val, b_val, c_val in product((0, 1), repeat=3):
        env: dict[str, bool] = {"a": bool(a_val), "b": bool(b_val), "c": bool(c_val)}
        result_flag: bool = is_rpn_true(rpn_tokens, env)
        print(a_val, b_val, c_val, int(result_flag))


task_18()


# +
class LogicTools19:
    """Namespace с хелперами для task_19."""

    TOKEN_PATTERN: str = r"and|or|not|\(|\)|[A-Z]"
    PRECEDENCE: dict[str, int] = {"not": 3, "and": 2, "or": 1}
    ASSOCIATIVITY: dict[str, str] = {
        "not": "right",
        "and": "left",
        "or": "left",
    }

    @staticmethod
    def is_operator_pop_required(current_op: str, top_op: str) -> bool:
        """Return True if top operator must be popped before pushing."""
        is_left: bool = LogicTools19.ASSOCIATIVITY[current_op] == "left"
        is_right: bool = LogicTools19.ASSOCIATIVITY[current_op] == "right"
        le_prec: bool = (
            LogicTools19.PRECEDENCE[current_op] <= LogicTools19.PRECEDENCE[top_op]
        )
        lt_prec: bool = (
            LogicTools19.PRECEDENCE[current_op] < LogicTools19.PRECEDENCE[top_op]
        )
        return (is_left and le_prec) or (is_right and lt_prec)

    @staticmethod
    def to_rpn(tokens: list[str]) -> list[str]:
        """Convert infix tokens to Reverse Polish Notation."""
        output: list[str] = []
        op_stack: list[str] = []
        for token in tokens:
            if re.fullmatch(r"[A-Z]", token):
                output.append(token)
            elif token == "(":
                op_stack.append(token)
            elif token == ")":
                while op_stack and op_stack[-1] != "(":
                    output.append(op_stack.pop())
                op_stack.pop()
            else:
                while op_stack and op_stack[-1] != "(":
                    top_op: str = op_stack[-1]
                    need_pop: bool = LogicTools19.is_operator_pop_required(
                        token, top_op
                    )
                    if not need_pop:
                        break
                    output.append(op_stack.pop())
                op_stack.append(token)
        while op_stack:
            output.append(op_stack.pop())
        return output

    @staticmethod
    def is_rpn_true(postfix_tokens: list[str], environment: dict[str, bool]) -> bool:
        """Evaluate RPN boolean expression for environment."""
        stack_values: list[bool] = []
        for symbol in postfix_tokens:
            if symbol in environment:
                stack_values.append(environment[symbol])
            elif symbol == "not":
                operand: bool = stack_values.pop()
                stack_values.append(not operand)
            else:
                right_value: bool = stack_values.pop()
                left_value: bool = stack_values.pop()
                is_and: bool = symbol == "and"
                stack_values.append(
                    (left_value and right_value)
                    if is_and
                    else (left_value or right_value)
                )
        return stack_values[0]


def task_19() -> None:
    """Build truth table for expression with uppercase variables."""
    raw_expression: str = input().strip()
    tokens: list[str] = re.findall(LogicTools19.TOKEN_PATTERN, raw_expression)
    rpn_tokens: list[str] = LogicTools19.to_rpn(tokens)

    variable_names: list[str] = sorted(
        {tok for tok in tokens if re.fullmatch(r"[A-Z]", tok)}
    )
    print(*variable_names, "F")

    for bits in product((0, 1), repeat=len(variable_names)):
        environment: dict[str, bool] = {
            name: bool(bit) for name, bit in zip(variable_names, bits)
        }
        truth_value: bool = LogicTools19.is_rpn_true(rpn_tokens, environment)
        print(*bits, int(truth_value))


task_19()

# +
BoolBinOp = Callable[[bool, bool], bool]


class LogicTools20:
    """Helpers for task_20 with ->, ^, ~ operators."""

    TOKEN_PATTERN: ClassVar[str] = r"->|not|and|or|\^|~|\(|\)|[A-Z]"
    PRECEDENCE: ClassVar[dict[str, int]] = {
        "not": 5,
        "and": 4,
        "or": 3,
        "^": 2,
        "->": 1,
        "~": 0,
    }
    ASSOCIATIVITY: ClassVar[dict[str, str]] = {
        "not": "right",
        "and": "left",
        "or": "left",
        "^": "left",
        "->": "right",
        "~": "left",
    }
    BINARY_OPS: ClassVar[dict[str, BoolBinOp]] = {
        "and": (lambda left_value, right_value: left_value and right_value),
        "or": (lambda left_value, right_value: left_value or right_value),
        "^": (lambda left_value, right_value: left_value != right_value),
        "->": (lambda left_value, right_value: (not left_value) or right_value),
        "~": (lambda left_value, right_value: left_value == right_value),
    }

    @staticmethod
    def is_operator_pop_required(current_op: str, top_op: str) -> bool:
        """Return True if top operator must be popped before pushing."""
        is_left: bool = LogicTools20.ASSOCIATIVITY[current_op] == "left"
        is_right: bool = LogicTools20.ASSOCIATIVITY[current_op] == "right"
        le_prec: bool = (
            LogicTools20.PRECEDENCE[current_op] <= LogicTools20.PRECEDENCE[top_op]
        )
        lt_prec: bool = (
            LogicTools20.PRECEDENCE[current_op] < LogicTools20.PRECEDENCE[top_op]
        )
        return (is_left and le_prec) or (is_right and lt_prec)

    @staticmethod
    def to_rpn(tokens: list[str]) -> list[str]:
        """Convert infix tokens to Reverse Polish Notation."""
        output: list[str] = []
        op_stack: list[str] = []
        for token in tokens:
            if re.fullmatch(r"[A-Z]", token):
                output.append(token)
            elif token == "(":
                op_stack.append(token)
            elif token == ")":
                while op_stack and op_stack[-1] != "(":
                    output.append(op_stack.pop())
                op_stack.pop()
            else:
                while op_stack and op_stack[-1] != "(":
                    top_op: str = op_stack[-1]
                    need_pop: bool = LogicTools20.is_operator_pop_required(
                        token, top_op
                    )
                    if not need_pop:
                        break
                    output.append(op_stack.pop())
                op_stack.append(token)
        while op_stack:
            output.append(op_stack.pop())
        return output

    @staticmethod
    def is_rpn_true(postfix_tokens: list[str], environment: dict[str, bool]) -> bool:
        """Evaluate RPN boolean expression for environment."""
        stack_values: list[bool] = []
        for symbol in postfix_tokens:
            if symbol in environment:
                stack_values.append(environment[symbol])
            elif symbol == "not":
                operand: bool = stack_values.pop()
                stack_values.append(not operand)
            else:
                right_value: bool = stack_values.pop()
                left_value: bool = stack_values.pop()
                apply_op: BoolBinOp = LogicTools20.BINARY_OPS[symbol]
                stack_values.append(apply_op(left_value, right_value))
        return stack_values[0]


def task_20() -> None:
    """Build truth table for expression with ->, ^, and ~ operators."""
    raw_expression: str = input().strip()
    tokens: list[str] = re.findall(LogicTools20.TOKEN_PATTERN, raw_expression)
    rpn_tokens: list[str] = LogicTools20.to_rpn(tokens)

    variable_names: list[str] = sorted(
        {tok for tok in tokens if re.fullmatch(r"[A-Z]", tok)}
    )
    print(*variable_names, "F")

    for bits in product((0, 1), repeat=len(variable_names)):
        environment: dict[str, bool] = {
            name: bool(bit) for name, bit in zip(variable_names, bits)
        }
        truth_value: bool = LogicTools20.is_rpn_true(rpn_tokens, environment)
        print(*bits, int(truth_value))


task_20()
