"""Working with built-in functions from python and itertools."""

# +
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
# def task_18() -> None:
#     """Build truth table for expression in a, b, c without eval."""
#     expression_text: str = input().strip()
#     tokens: list[str] = expression_text.split()

#     # Operator precedence and associativity
#     precedence: dict[str, int] = {"not": 3, "and": 2, "or": 1}
#     associativity: dict[str, str] = {
#         "not": "right",
#         "and": "left",
#         "or": "left",
#     }

#     # Shunting-yard to convert to RPN
#     output_queue: list[str] = []
#     operator_stack: list[str] = []
#     for token in tokens:
#         if token in ("a", "b", "c"):
#             output_queue.append(token)
#         elif token == "(":
#             operator_stack.append(token)
#         elif token == ")":
#             while operator_stack and operator_stack[-1] != "(":
#                 output_queue.append(operator_stack.pop())
#             operator_stack.pop()
#         else:
#             # token is an operator: not, and, or
#             while (
#                 operator_stack
#                 and operator_stack[-1] != "("
#                 and (
#                     associativity[token] == "left"
#                     and precedence[token] <= precedence[operator_stack[-1]]
#                     or associativity[token] == "right"
#                     and precedence[token] < precedence[operator_stack[-1]]
#                 )
#             ):
#                 output_queue.append(operator_stack.pop())
#             operator_stack.append(token)
#     while operator_stack:
#         output_queue.append(operator_stack.pop())

#     # Evaluate RPN without eval
#     def apply_unary(op: str, stack: list[bool]) -> None:
#         operand: bool = stack.pop()
#         stack.append(not operand)

#     def apply_binary(op: str, stack: list[bool]) -> None:
#         right: bool = stack.pop()
#         left: bool = stack.pop()
#         if op == "and":
#             stack.append(left and right)
#         elif op == "or":
#             stack.append(left or right)

#     # Print header
#     print("a b c f")
#     # Iterate all 0/1 assignments
#     for a_val, b_val, c_val in product((0, 1), repeat=3):
#         env: dict[str, bool] = {
#             "a": bool(a_val),
#             "b": bool(b_val),
#             "c": bool(c_val),
#         }
#         stack_eval: list[bool] = []
#         for token in output_queue:
#             if token in env:
#                 stack_eval.append(env[token])
#             elif token == "not":
#                 apply_unary(token, stack_eval)
#             else:  # 'and' or 'or'
#                 apply_binary(token, stack_eval)

#         result_flag: bool = stack_eval[0]
#         print(a_val, b_val, c_val, int(result_flag))


# task_18()

# +
# def task_19() -> None:
#     """Build truth table for expression with uppercase variables."""
#     raw_expression: str = input().strip()

#     # Tokenize into variables, operators, and parentheses
#     token_pattern: str = r"and|or|not|\(|\)|[A-Z]"
#     tokens: list[str] = re.findall(token_pattern, raw_expression)

#     # Operator precedence and associativity
#     precedence: dict[str, int] = {"not": 3, "and": 2, "or": 1}
#     associativity: dict[str, str] = {
#         "not": "right",
#         "and": "left",
#         "or": "left",
#     }

#     # Shunting-yard: convert to Reverse Polish Notation
#     rpn_queue: list[str] = []
#     operator_stack: list[str] = []
#     for symbol in tokens:
#         if re.fullmatch(r"[A-Z]", symbol):
#             rpn_queue.append(symbol)
#         elif symbol == "(":
#             operator_stack.append(symbol)
#         elif symbol == ")":
#             while operator_stack and operator_stack[-1] != "(":
#                 rpn_queue.append(operator_stack.pop())
#             operator_stack.pop()
#         else:
#             # symbol is an operator
#             while (
#                 operator_stack
#                 and operator_stack[-1] != "("
#                 and (
#                     associativity[symbol] == "left"
#                     and precedence[symbol] <= precedence[operator_stack[-1]]
#                     or associativity[symbol] == "right"
#                     and precedence[symbol] < precedence[operator_stack[-1]]
#                 )
#             ):
#                 rpn_queue.append(operator_stack.pop())
#             operator_stack.append(symbol)
#     while operator_stack:
#         rpn_queue.append(operator_stack.pop())

#     # Gather and sort variable names
#     variable_names: list[str] = sorted(
#         {sym for sym in tokens if re.fullmatch(r"[A-Z]", sym)}
#     )
#     print(*variable_names, "F")

#     # Evaluate RPN for each assignment of 0/1
#     for assignment in product((0, 1), repeat=len(variable_names)):
#         environment: dict[str, bool] = {
#             var_name: bool(bit) for var_name, bit in zip(variable_names,
# assignment)
#         }
#         evaluation_stack: list[bool] = []
#         for symbol in rpn_queue:
#             if symbol in environment:
#                 evaluation_stack.append(environment[symbol])
#             elif symbol == "not":
#                 operand_value: bool = evaluation_stack.pop()
#                 evaluation_stack.append(not operand_value)
#             else:
#                 right_value: bool = evaluation_stack.pop()
#                 left_value: bool = evaluation_stack.pop()
#                 if symbol == "and":
#                     evaluation_stack.append(left_value and right_value)
#                 else:  # symbol == 'or'
#                     evaluation_stack.append(left_value or right_value)
#         truth_value: bool = evaluation_stack[0]
#         print(*assignment, int(truth_value))


# task_19()

# +
# import re
# from itertools import product


# def task_20() -> None:
#     """Build truth table for expression with ->, ^, and ~ operators."""
#     raw_expression: str = input().strip()

#     # Tokenize into variables, operators, and parentheses
#     token_pattern = r'->|not|and|or|\^|~|\(|\)|[A-Z]'
#     tokens: list[str] = re.findall(token_pattern, raw_expression)

#     # Operator precedence and associativity
#     precedence: dict[str, int] = {
#         'not': 5,
#         'and': 4,
#         'or': 3,
#         '^': 2,
#         '->': 1,
#         '~': 0,
#     }
#     associativity: dict[str, str] = {
#         'not': 'right',
#         'and': 'left',
#         'or': 'left',
#         '^': 'left',
#         '->': 'right',
#         '~': 'left',
#     }

#     # Shunting-yard algorithm to get Reverse Polish Notation (RPN)
#     output_queue: list[str] = []
#     operator_stack: list[str] = []
#     for token in tokens:
#         if re.fullmatch(r'[A-Z]', token):
#             output_queue.append(token)
#         elif token == '(':
#             operator_stack.append(token)
#         elif token == ')':
#             while operator_stack and operator_stack[-1] != '(':
#                 output_queue.append(operator_stack.pop())
#             operator_stack.pop()
#         else:
#             # operator
#             while (
#                 operator_stack and operator_stack[-1] != '(' and
#                 ((associativity[token] == 'left' and
#                   precedence[token] <= precedence[operator_stack[-1]]) or
#                  (associativity[token] == 'right' and
#                   precedence[token] < precedence[operator_stack[-1]]))
#             ):
#                 output_queue.append(operator_stack.pop())
#             operator_stack.append(token)
#     while operator_stack:
#         output_queue.append(operator_stack.pop())

#     # Boolean operation implementations
#     def is_negation(value: bool) -> bool:
#         return not value

#     def is_conjunction(left: bool, right: bool) -> bool:
#         return left and right

#     def is_disjunction(left: bool, right: bool) -> bool:
#         return left or right

#     def is_strict_disjunction(left: bool, right: bool) -> bool:
#         return left != right

#     def is_implication(left: bool, right: bool) -> bool:
#         return (not left) or right

#     def is_equivalence(left: bool, right: bool) -> bool:
#         return left == right

#     # Gather and sort variable names
#     variable_names: list[str] = sorted({
#         tok for tok in tokens if re.fullmatch(r'[A-Z]', tok)
#     })
#     print(*variable_names, "F")

#     # Evaluate for each combination of variable assignments
#     for combo in product((0, 1), repeat=len(variable_names)):
#         environment: dict[str, bool] = {
#             var: bool(bit) for var, bit in zip(variable_names, combo)
#         }
#         evaluation_stack: list[bool] = []
#         for token in output_queue:
#             if token == 'not':
#                 operand = evaluation_stack.pop()
#                 evaluation_stack.append(is_negation(operand))
#             elif token in ('and', 'or', '^', '->', '~'):
#                 right_operand = evaluation_stack.pop()
#                 left_operand = evaluation_stack.pop()
#                 if token == 'and':
#                     evaluation_stack.append(is_conjunction(left_operand,
# right_operand))
#                 elif token == 'or':
#                     evaluation_stack.append(is_disjunction(left_operand,
# right_operand))
#                 elif token == '^':
#                     evaluation_stack.append(is_strict_disjunction
# (left_operand, right_operand)) !!
#                 elif token == '->':
#                     evaluation_stack.append(is_implication(left_operand,
# right_operand))
#                 else:
#                     evaluation_stack.append(is_equivalence(left_operand,
# right_operand))
#             else:
#                 evaluation_stack.append(environment[token])
#         final_value = evaluation_stack[0]
#         print(*combo, int(final_value))


# task_20()
