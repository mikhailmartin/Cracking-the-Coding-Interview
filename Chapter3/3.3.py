class StackError(BaseException):
    ...


class FullStackError(StackError):
    ...


class EmptyStackError(StackError):
    ...


class Stack(list):
    def __init__(self, size: int) -> None:
        super().__init__()
        self.size = size

    push = list.append

    def peek(self):
        return self[-1]

    def is_full(self) -> bool:
        return len(self) == self.size

    def is_empty(self) -> bool:
        return len(self) == 0


class SetOfStacks:
    stack_size = 1024

    def __init__(self) -> None:
        self.set_of_stacks: list[Stack] = []

    def push(self, value: int) -> None:
        if self.is_empty() or self.set_of_stacks[-1].is_full():
            self.set_of_stacks.append(Stack(self.stack_size))
        self.set_of_stacks[-1].append(value)

    def pop(self) -> int:
        if self.is_empty():
            raise EmptyStackError()
        value = self.set_of_stacks[-1].pop()
        if self.set_of_stacks[-1].is_empty():
            self.set_of_stacks.pop()
        return value

    def pop_at(self):
        ...

    def is_empty(self) -> bool:
        return len(self.set_of_stacks) == 0
