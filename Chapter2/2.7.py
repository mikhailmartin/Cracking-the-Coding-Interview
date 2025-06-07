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
        self.length: int = 0

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

    def concatenate(self, other: Self) -> None:
        if isinstance(other, LinkedList):
            self.last.next = other.first
            self.last = other.last
            self.length += other.length

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
        self.append_node(new_node)

    def append_node(self, node: Node) -> None:
        if self.last is None:
            self.last = node
            self.first = self.last
        else:
            self.last.next = node
            self.last = node
        self.length += 1

    def drop_duplicates(self) -> None:
        current_node = self.first
        while current_node is not None:
            nested_current_node = current_node.next
            previous_node = current_node
            while nested_current_node is not None:
                if nested_current_node.value == current_node.value:
                    previous_node.next = nested_current_node.next
                    self.length -= 1
                else:
                    previous_node = nested_current_node
                nested_current_node = nested_current_node.next
            current_node = current_node.next

    @staticmethod
    def remove_item(node: Node) -> None:
        node.value = node.next.value
        node.next = node.next.next
        # self.length -= 1  # TODO

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

        before.concatenate(after)
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

    def find_intersection(self, other: Self) -> bool | Node:

        if self.last is not other.last or self.length == 0 or other.length == 0:
            return False

        difference = self.length - other.length
        self_node = self.first
        other_node = other.first
        if difference > 0:
            for _ in range(difference):
                self_node = self_node.next
        else:
            for _ in range(-difference):
                other_node = other_node.next
        while self_node is not None:
            if self_node is other_node:
                return self_node
            else:
                self_node = self_node.next
                other_node = other_node.next
        return False


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

    left_linked_list = LinkedList()
    left_linked_list.append_node(Node(1))
    left_linked_list.append_node(Node(2))
    left_linked_list.append_node(Node(3))

    right_linked_list = LinkedList()
    right_linked_list.append_node(Node(4))
    right_linked_list.append_node(Node(5))
    right_linked_list.append_node(Node(6))

    tail_linked_list = LinkedList()
    tail_linked_list.append_node(Node(7))
    tail_linked_list.append_node(Node(8))
    tail_linked_list.append_node(Node(9))

    left_linked_list.append_node(tail_linked_list.first)
    right_linked_list.append_node(tail_linked_list.first)

    print(left_linked_list.find_intersection(right_linked_list))
