from collections import namedtuple


NodeWithMin = namedtuple("NodeWithMin", ["value", "minimum"])


class StackError(BaseException):
    ...


class FullStackError(StackError):
    ...


class EmptyStackError(StackError):
    ...


class StackWithMin:
    def __init__(self) -> None:
        self.items: list[NodeWithMin] = []

    def push(self, value: int) -> None:
        minimum = value if self.is_empty() else min(value, self.min())
        self.items.append(NodeWithMin(value, minimum))

    def pop(self) -> int:
        if self.is_empty():
            raise EmptyStackError()
        node = self.items.pop()
        return node.value

    def peek(self) -> int:
        if self.is_empty():
            raise EmptyStackError()
        return self.items[-1].value

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def min(self) -> int:
        return self.items[-1].minimum


class StackWithMin2:
    def __init__(self) -> None:
        self.items = []
        self.minimums = []

    def push(self, value: int) -> None:
        if self.is_empty() or value <= self.min():
            self.minimums.append(value)
        self.items.append(value)

    def pop(self) -> int:
        value = self.items.pop()
        if value == self.min():
            self.minimums.pop()
        return value

    def peek(self) -> int:
        return self.items[-1]

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def min(self) -> int:
        return self.minimums[-1]
