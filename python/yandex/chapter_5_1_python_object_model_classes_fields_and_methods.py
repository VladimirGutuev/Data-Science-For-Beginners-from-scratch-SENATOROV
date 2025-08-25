"""Working with classes, fields and methods."""


class Point:
    """2D point with Cartesian coordinates."""

    x1: float | int
    y1: float | int

    def __init__(self, x_coordinate: float | int, y_coordinate: float | int) -> None:
        """Initialize point with x1 and y1 coordinates."""
        self.x1 = x_coordinate
        self.y1 = y_coordinate


class Point1:
    """2D point with Cartesian coordinates."""

    x2: float | int
    y2: float | int

    def __init__(self, x_coordinate: float | int, y_coordinate: float | int) -> None:
        """Initialize point with x2 and y2 coordinates."""
        self.x2 = x_coordinate
        self.y2 = y_coordinate

    def move(self, delta_x: float | int, delta_y: float | int) -> None:
        """Shift point along axes by given deltas."""
        self.x2 = self.x2 + delta_x
        self.y2 = self.y2 + delta_y

    def length(self, other: "Point1") -> float:
        """Return distance to another point rounded to hundredths."""
        delta_x: float = float(self.x2) - float(other.x2)
        delta_y: float = float(self.y2) - float(other.y2)
        distance: float = (delta_x * delta_x + delta_y * delta_y) ** 0.5
        return round(distance, 2)


class RedButton:
    """Red button that prints alarm and tracks clicks."""

    def __init__(self) -> None:
        """Initialize internal click counter."""
        self.counter: int = 0

    def click(self) -> None:
        """Print alarm and increment counter."""
        self.counter += 1
        print("Тревога!")

    def count(self) -> int:
        """Return number of times the button was clicked."""
        return self.counter


class Programmer:
    """Programmer with position-based hourly pay and promotions."""

    POSITIONS: dict[str, int] = {"Junior": 10, "Middle": 15, "Senior": 20}

    def __init__(self, name: str, position: str) -> None:
        """Initialize with name, position, zero hours and zero pay."""
        self.name: str = name
        self.position: str = position
        self.hours_worked: int = 0
        self.pay: int = 0
        self.hourly_rate: int = self.POSITIONS[position]

    def work(self, hours: int) -> None:
        """Accrue pay for given hours at current rate."""
        self.hours_worked += hours
        self.pay += self.hourly_rate * hours

    def rise(self) -> None:
        """Promote or increase Senior rate by one."""
        if self.position == "Senior":
            self.hourly_rate += 1
            return
        if self.position == "Junior":
            self.position = "Middle"
        else:
            self.position = "Senior"
        self.hourly_rate = self.POSITIONS[self.position]

    def info(self) -> str:
        """Return accounting summary."""
        return f"{self.name} {self.hours_worked}ч. {self.pay}тгр."


class Rectangle:
    """Axis-aligned rectangle from two opposite corner points."""

    x3: float
    y3: float
    width: float
    height: float

    def __init__(
        self,
        first: tuple[float | int, float | int],
        second: tuple[float | int, float | int],
    ) -> None:
        """Initialize rectangle from two opposite corners."""
        (x_first, y_first), (x_second, y_second) = first, second
        x_first, x_second = sorted((float(x_first), float(x_second)))
        y_first, y_second = sorted((float(y_first), float(y_second)))
        self.x3, self.y3 = x_first, y_first
        self.width, self.height = x_second - x_first, y_second - y_first

    def perimeter(self) -> float:
        """Return rectangle perimeter rounded to hundredths."""
        double_sum: float = 2.0 * (self.width + self.height)
        return round(double_sum, 2)

    def area(self) -> float:
        """Return rectangle area rounded to hundredths."""
        area_value: float = self.width * self.height
        return round(area_value, 2)


class Rectangle1:
    """Axis-aligned rectangle from two opposite corner points."""

    x4: float
    y4: float
    width: float
    height: float

    def __init__(
        self,
        first: tuple[float | int, float | int],
        second: tuple[float | int, float | int],
    ) -> None:
        """Initialize rectangle from two opposite corners."""
        (x_first, y_first), (x_second, y_second) = first, second
        x_first, x_second = sorted((float(x_first), float(x_second)))
        y_first, y_second = sorted((float(y_first), float(y_second)))
        self.x4, self.y4 = x_first, y_first
        self.width, self.height = x_second - x_first, y_second - y_first

    def perimeter(self) -> float:
        """Return rectangle perimeter rounded to hundredths."""
        double_sum: float = 2.0 * (self.width + self.height)
        return round(double_sum, 2)

    def area(self) -> float:
        """Return rectangle area rounded to hundredths."""
        area_value: float = self.width * self.height
        return round(area_value, 2)

    def get_pos(self) -> tuple[float, float]:
        """Return coordinates of the top-left corner."""
        top_left_y: float = self.y4 + self.height
        return round(self.x4, 2), round(top_left_y, 2)

    def get_size(self) -> tuple[float, float]:
        """Return rectangle size as (width, height)."""
        return round(self.width, 2), round(self.height, 2)

    def move(self, delta_x: float | int, delta_y: float | int) -> None:
        """Shift rectangle by given deltas."""
        self.x4 = self.x4 + float(delta_x)
        self.y4 = self.y4 + float(delta_y)

    def resize(self, new_width: float | int, new_height: float | int) -> None:
        """Resize keeping the top-left corner fixed."""
        fixed_top_y: float = self.y4 + self.height
        self.width = float(new_width)
        self.height = float(new_height)
        self.y4 = fixed_top_y - self.height


class Rectangle2:
    """Axis-aligned rectangle from two opposite corner points."""

    x5: float
    y5: float
    width: float
    height: float

    def __init__(
        self,
        first: tuple[float | int, float | int],
        second: tuple[float | int, float | int],
    ) -> None:
        """Initialize rectangle from two opposite corners."""
        (x_first, y_first), (x_second, y_second) = first, second
        x_first, x_second = sorted((float(x_first), float(x_second)))
        y_first, y_second = sorted((float(y_first), float(y_second)))
        self.x5, self.y5 = x_first, y_first
        self.width, self.height = x_second - x_first, y_second - y_first

    def perimeter(self) -> float:
        """Return rectangle perimeter rounded to hundredths."""
        double_sum: float = 2.0 * (self.width + self.height)
        return round(double_sum, 2)

    def area(self) -> float:
        """Return rectangle area rounded to hundredths."""
        area_value: float = self.width * self.height
        return round(area_value, 2)

    def get_pos(self) -> tuple[float, float]:
        """Return coordinates of the top-left corner."""
        top_left_y: float = self.y5 + self.height
        return round(self.x5, 2), round(top_left_y, 2)

    def get_size(self) -> tuple[float, float]:
        """Return rectangle size as (width, height)."""
        return round(self.width, 2), round(self.height, 2)

    def move(self, delta_x: float | int, delta_y: float | int) -> None:
        """Shift rectangle by given deltas."""
        self.x5 = self.x5 + float(delta_x)
        self.y5 = self.y5 + float(delta_y)

    def resize(self, new_width: float | int, new_height: float | int) -> None:
        """Resize keeping the top-left corner fixed."""
        fixed_top_y: float = self.y5 + self.height
        self.width = float(new_width)
        self.height = float(new_height)
        self.y5 = fixed_top_y - self.height

    def turn(self) -> None:
        """Rotate 90° clockwise around center with rounding to hundredths."""
        center_x: float = self.x5 + self.width / 2.0
        center_y: float = self.y5 + self.height / 2.0
        new_width: float = round(self.height, 2)
        new_height: float = round(self.width, 2)
        self.width, self.height = new_width, new_height
        self.x5 = round(center_x - self.width / 2.0, 2)
        self.y5 = round(center_y - self.height / 2.0, 2)

    def scale(self, factor: float | int) -> None:
        """Scale size by factor around center with rounding to hundredths."""
        center_x: float = self.x5 + self.width / 2.0
        center_y: float = self.y5 + self.height / 2.0
        scaled_width: float = round(self.width * float(factor), 2)
        scaled_height: float = round(self.height * float(factor), 2)
        self.width, self.height = scaled_width, scaled_height
        self.x5 = round(center_x - self.width / 2.0, 2)
        self.y5 = round(center_y - self.height / 2.0, 2)


# +
class Cell:
    """Board cell with state: 'W', 'B', or 'X' (empty)."""

    def __init__(self, initial_state: str) -> None:
        """Initialize cell with given state."""
        self._state: str = initial_state

    def status(self) -> str:
        """Return stored state."""
        return self._state

    def set_state(self, new_state: str) -> None:
        """Update stored state."""
        self._state = new_state


class Checkers:
    """Checkers board with standard initial placement."""

    def __init__(self) -> None:
        """Build 8x8 board with initial pieces."""
        self.cells: dict[str, Cell] = {}
        for row_char in "12345678":
            row_num: int = int(row_char)
            for col_index, col_char in enumerate("ABCDEFGH"):
                position: str = f"{col_char}{row_char}"
                is_dark_square: bool = (col_index + row_num) % 2 == 1
                state: str = "X"
                if row_num >= 6 and is_dark_square:
                    state = "B"
                elif row_num <= 3 and is_dark_square:
                    state = "W"
                self.cells[position] = Cell(state)

    def move(self, from_pos: str, to_pos: str) -> None:
        """Move a piece from from_pos to to_pos."""
        source_cell: Cell = self.cells[from_pos]
        target_cell: Cell = self.cells[to_pos]
        moving_state: str = source_cell.status()
        if moving_state != "X":
            target_cell.set_state(moving_state)
            source_cell.set_state("X")

    def get_cell(self, position: str) -> Cell:
        """Return cell object at position like 'A1'."""
        return self.cells[position]


# -


class Queue:
    """FIFO queue implemented via singly linked list."""

    class _Node:
        """List node storing a value and next pointer."""

        __slots__ = ("value", "next")

        def __init__(self, value: object) -> None:
            """Initialize node with value."""
            self.value: object = value
            self.next: "Queue._Node | None" = None

    def __init__(self) -> None:
        """Initialize empty queue."""
        self._head: "Queue._Node | None" = None
        self._tail: "Queue._Node | None" = None

    def push(self, item: object) -> None:
        """Add item to the end of the queue."""
        new_node: Queue._Node = Queue._Node(item)
        tail = self._tail
        if tail is None:
            self._head = new_node
            self._tail = new_node
            return
        tail.next = new_node
        self._tail = new_node

    def pop(self) -> object:
        """Remove and return the first item of the queue."""
        head = self._head
        if head is None:
            raise IndexError("pop from empty queue")
        value: object = head.value
        self._head = head.next
        if self._head is None:
            self._tail = None
        return value

    def is_empty(self) -> bool:
        """Return True if queue has no items."""
        return self._head is None


class Stack:
    """LIFO stack implemented via singly linked list."""

    class _Node:
        """List node storing a value and next pointer."""

        __slots__ = ("value", "next")

        def __init__(self, value: object) -> None:
            """Initialize node with value."""
            self.value: object = value
            self.next: "Stack._Node | None" = None

    def __init__(self) -> None:
        """Initialize empty stack."""
        self._head: "Stack._Node | None" = None

    def push(self, item: object) -> None:
        """Add item to the top of the stack."""
        new_node: Stack._Node = Stack._Node(item)
        new_node.next = self._head
        self._head = new_node

    def pop(self) -> object:
        """Remove and return the top item of the stack."""
        head = self._head
        if head is None:
            raise IndexError("pop from empty stack")
        value: object = head.value
        self._head = head.next
        return value

    def is_empty(self) -> bool:
        """Return True if stack has no items."""
        return self._head is None
