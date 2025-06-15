class StackError(BaseException):
    ...


class FullStackError(StackError):
    ...


class EmptyStackError(StackError):
    ...


class FixedMultiStack:
    number_of_stacks: int = 3

    def __init__(self, stack_size: int) -> None:
        self.stack_size = stack_size
        self.values = [0] * stack_size * self.number_of_stacks
        self.sizes = [0] * self.number_of_stacks

    def push(self, stack_num: int, value: int) -> None:
        """Занесение значения в стек."""
        if self.is_full(stack_num):
            raise FullStackError()
        self.values[self.index_of_top(stack_num)] = value
        self.sizes[stack_num] += 1

    def pop(self, stack_num: int) -> int:
        """Извлечение элемента стека."""
        if self.is_empty(stack_num):
            raise EmptyStackError()
        top_index = self.index_of_top(stack_num)
        value = self.values[top_index]
        self.values[top_index] = 0
        self.sizes[top_index] -= 1
        return value

    def peek(self, stack_num: int) -> int:
        """Просмотр элемента стека."""
        if self.is_empty(stack_num):
            raise EmptyStackError()
        return self.values[self.index_of_top(stack_num)]

    def is_full(self, stack_num: int) -> bool:
        """Проверка заполненного стека."""
        return self.sizes[stack_num] == self.stack_size

    def is_empty(self, stack_num: int) -> bool:
        """Проверка пустого стека."""
        return self.sizes[stack_num] == 0

    def index_of_top(self, stack_num: int) -> int:
        """Получение индекса вершины стека."""
        offset = stack_num * self.stack_size
        size = self.sizes[stack_num]
        return offset + size
