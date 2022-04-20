import warnings
from typing import Literal, Tuple

from base_classes import LinkedNode, LinkedList

class CircularLinkedList(LinkedList):  # noqa
    def __str__(self):
        if self.head == None:
            return '[]'
        if self.size == 1:
            return f'[{self.head.value}]'
        return super().__str__() + "-> ..."

    def ordenar(self, which: Literal['m', 'q', 'i', 'b'] = "m"):  # TODO mudar para o mais efetivo
        return super().ordenar(which)

    def append(self, item):
        if self.size == 0:
            self.head = LinkedNode(item)
            self.tail = self.head
        else:
            self.tail.next = LinkedNode(item)
            self.tail = self.tail.next
        self.tail.next = self.head
        self.size += 1

    def prepend(self, item):
        if self.size == 0:
            return self.append(item)
        else:
            self.tail.next = LinkedNode(item, self.head)
            self.head = self.tail.next
        self.size += 1

    def ins(self, item):
        return self.append(item)

    def rem(self, item):
        return self.RemoveFirst(item)

    # removes first found
    def RemoveFirst(self, item):
        prev = None
        for i in self:
            if i.value == item:
                if prev is None:
                    # data is in head
                    self.head = self.head.next
                    self.tail.next = self.head
                else:
                    prev.next = i.next
                return
            prev = i
        return False

    def bubbleSort(self):#Todo need test
        is_sorted = False
        while not is_sorted:
            is_sorted = True
            current_node = self.head
            while current_node.next is not None:
                if current_node.value > current_node.next.value:
                    LinkedNode.swap(current_node, current_node.next)
                    is_sorted = False
                current_node = current_node.next

    def binarySearch(self, item, order=False) -> Tuple[LinkedNode | None, int]: # TODO change to True default
        #TODO test
        if order:
            self.ordenar()
        start = (self.head, 0)
        end = (self.tail, self.size - 1)
        while end[0] != start[0] or end[0] is None or start[0] is None:  # not sure of this line
            mid = self.findMiddle(start, end)
            if mid[0].value == item:
                return mid
            elif mid[0].value > item:
                start = (mid[0].next, mid[1] + 1)
            else:
                end = mid
        return None, -1

if __name__ == "__main__":
    # tests TODO
    pass