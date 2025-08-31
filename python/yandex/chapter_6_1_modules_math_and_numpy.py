"""Working with modules math and numpy."""

import sys
from math import comb, cos, dist, e, gcd, log, pi, prod, sin

import numpy as np


def task_1() -> None:
    """Compute f(x) from input per given formula and print the result."""
    input_value: float = float(input())

    log_term: float = log(input_value ** (3.0 / 16.0), 32.0)

    cos_argument: float = (pi * input_value) / (2.0 * e)
    power_term: float = input_value ** cos(cos_argument)

    sine_square: float = sin(input_value / pi) ** 2

    result_value: float = log_term + power_term - sine_square
    print(result_value)


task_1()


def task_2() -> None:
    """Print GCD for each whitespace-separated integer line from stdin."""
    for input_row in sys.stdin:
        stripped: str = input_row.strip()
        if not stripped:
            continue
        values: list[int] = [int(piece) for piece in stripped.split()]
        result_value: int = gcd(*values)
        print(result_value)


task_2()


def task_3() -> None:
    """Print combos with Vasya included and total combos."""
    total_people, seats_count = map(int, input().split())
    favorable: int = comb(total_people - 1, seats_count - 1)
    total: int = comb(total_people, seats_count)
    print(f"{favorable} {total}")


task_3()


def task_4() -> None:
    """Print geometric mean of whitespace-separated positive numbers."""
    input_row: str = input().strip()
    numbers = np.asarray([float(piece) for piece in input_row.split()])
    values_count: int = int(numbers.size)
    product_value: float = float(prod(numbers))
    mean_value: float = product_value ** (1.0 / values_count)
    print(mean_value)


task_4()


def task_5() -> None:
    """Print distance between (x, y) and (rho, phi) after polar->cartesian."""
    cartesian_x, cartesian_y = map(float, input().split())
    polar_rho, polar_phi = map(float, input().split())

    polar_x: float = polar_rho * cos(polar_phi)
    polar_y: float = polar_rho * sin(polar_phi)

    distance_value: float = dist([cartesian_x, cartesian_y], [polar_x, polar_y])
    print(distance_value)


task_5()


def multiplication_matrix(size: int) -> object:
    """Return an NxN multiplication table as a NumPy integer array."""
    numbers = np.arange(1, size + 1, dtype=int)
    result = np.multiply.outer(numbers, numbers)
    return result


def make_board(board_size: int) -> object:
    """Return an NxN chessboard matrix (1=white, 0=black) with dtype int8."""
    board = np.zeros((board_size, board_size), dtype=np.int8)
    board[::2, ::2] = 1
    board[1::2, 1::2] = 1
    return board


def snake(width: int, height: int, direction: str = "H") -> object:
    """Return MxN snake matrix (H=horizontal, V=vertical) with dtype int16."""
    total_values: int = width * height
    base = np.arange(1, total_values + 1, dtype=np.int16)
    dir_upper: str = direction.upper()

    if dir_upper == "H":
        matrix = base.reshape(height, width)
        matrix[1::2, :] = matrix[1::2, ::-1]
        return matrix

    if dir_upper == "V":
        matrix = base.reshape(height, width, order="F")
        matrix[:, 1::2] = matrix[::-1, 1::2]
        return matrix

    raise ValueError("direction must be 'H' or 'V'")


def rotate(matrix: object, angle: int) -> object:
    """Return a new matrix rotated clockwise by 90/180/270/360 degrees."""
    arr = np.asarray(matrix)
    if arr.ndim != 2:
        raise ValueError("matrix must be 2D")

    normalized: int = angle % 360
    if normalized == 0:
        return arr.copy()
    if normalized == 90:
        return np.transpose(arr)[:, ::-1].copy()
    if normalized == 180:
        return arr[::-1, ::-1].copy()
    if normalized == 270:
        return np.transpose(arr)[::-1, :].copy()

    raise ValueError("angle must be one of 90, 180, 270, 360")


def stairs(vector: object) -> object:
    """Return a matrix where row i is the input vector rolled right by i."""
    arr = np.asarray(vector)
    if arr.ndim != 1:
        raise ValueError("vector must be 1D")

    length: int = int(arr.shape[0])
    cols = np.arange(length)[None, :]
    rows = np.arange(length)[:, None]
    positions = (cols - rows) % length
    result = arr[positions]
    return result
