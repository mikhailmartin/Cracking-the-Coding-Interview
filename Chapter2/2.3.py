from typing import Any


class Node:
    def __init__(self, value: Any) -> None:
        self.value = value
        self.next: Any = None

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


if __name__ == "__main__":

    linked_list = LinkedList()
    linked_list.from_iterable([1, 2, 3, 4, 5])
    node = linked_list.first.next.next
    print(node)
    linked_list.remove_item(node)
    print(linked_list)
