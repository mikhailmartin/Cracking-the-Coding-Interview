from typing import Any, Self


class Node:
    def __init__(self, value: Any, next: Any = None) -> None:
        self.value = value
        self.next = next

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.value}, {self.next})"


class LinkedList:
    def __init__(self) -> None:
        self.first: Node | None = None
        self.last: Node | None = None

    def __repr__(self) -> str:
        values = []
        node = self.first
        while node is not None:
            values.append(str(node.value))
            node = node.next
        return f"{self.__class__.__name__}[{', '.join(values)}]"

    def __getitem__(self, index: int) -> Any:
        if index >= 0:
            raise NotImplemented
        else:
            return self.__getitem_negative(-index)

    def __delitem__(self, index: int) -> None:
        if index == 0:
            raise NotImplemented

        i = 1
        previous_node = self.first
        current_node = self.first.next
        while i != index:
            previous_node = previous_node.next
            current_node = current_node.next
            i += 1
        previous_node.next = current_node.next

    def add(self, other) -> None:
        if isinstance(other, LinkedList):
            self.last.next = other.first
            self.last = other.last

    def __getitem_negative(self, index: int) -> int:

        p1 = self.first
        for _ in range(index):
            p1 = p1.next
        p2 = self.first

        while p1 is not None:
            p1 = p1.next
            p2 = p2.next

        return p2.value

    def from_iterable(self, iterable) -> None:
        for elem in iterable:
            self.append(elem)

    def append(self, value) -> None:
        new_node = Node(value)
        if self.last is None:
            self.last = new_node
            self.first = self.last
        else:
            self.last.next = new_node
            self.last = new_node

    def drop_duplicates(self) -> None:
        current_node = self.first
        while current_node is not None:
            nested_current_node = current_node.next
            previous_node = current_node
            while nested_current_node is not None:
                if nested_current_node.value == current_node.value:
                    previous_node.next = nested_current_node.next
                else:
                    previous_node = nested_current_node
                nested_current_node = nested_current_node.next
            current_node = current_node.next

    @staticmethod
    def remove_item(node: Node) -> None:
        node.value = node.next.value
        node.next = node.next.next

    def split(self, split_value: int) -> None:

        before = LinkedList()
        after = LinkedList()

        node = self.first
        while node is not None:
            if node.value < split_value:
                before.append(node.value)
            else:
                after.append(node.value)
            node = node.next

        before.add(after)
        self.first = before.first
        self.last = before.last

    def is_palindrome(self) -> bool:
        if self.first is None or self.first.next is None:
            return True

        # Находим середину списка с помощью быстрого и медленного указателей
        slow = fast = self.first
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Разворачиваем вторую половину списка
        prev = None
        while slow is not None:
            current = Node(slow.value, prev)
            prev = current
            slow = slow.next

        # Сравниваем первую и развёрнутую вторую половины
        left, right = self.first, prev
        while right is not None:
            if left.value != right.value:
                return False
            left = left.next
            right = right.next

        return True


class NumberLinkedList(LinkedList):
    def __init__(self, number: int | None = None) -> None:
        super().__init__()
        if number == 0:
            self.append(number)
        while number:
            number, figure = divmod(number, 10)
            self.append(figure)

    def __add__(self, other) -> Self:
        if isinstance(other, NumberLinkedList):

            result = NumberLinkedList()

            left_node = self.first
            right_node = other.first

            carry = 0
            while left_node is not None and right_node is not None:
                carry, figure = divmod(left_node.value + right_node.value + carry, 10)
                result.append(figure)
                left_node = left_node.next
                right_node = right_node.next
            while left_node is not None:
                carry, figure = divmod(left_node.value + carry, 10)
                result.append(figure)
                left_node = left_node.next
            while right_node is not None:
                carry, figure = divmod(right_node.value + carry, 10)
                result.append(figure)
                right_node = right_node.next
            if carry:
                result.append(carry)

            return result

        else:
            raise NotImplemented

    def as_number(self) -> int:
        node = self.first
        result = 0
        power = 0
        while node is not None:
            result += node.value * pow(10, power)
            power += 1
            node = node.next
        return result


if __name__ == "__main__":

    linked_list = LinkedList()
    linked_list.from_iterable([5, 4, 3, 4, 5])
    print(linked_list.is_palindrome())
