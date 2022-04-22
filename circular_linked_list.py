import warnings
from typing import Literal, Tuple

from base_classes import LinkedNode, LinkedList


class CircularLinkedList(LinkedList):  # noqa
    def __str__(self):
        if self.head is None:
            return 'Empty'
        return super().__str__() + " -> / " + str(self.head.value) + " -> ... "

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

    def ins(self, item):
        return self.append(item)

    def prepend(self, item):
        if self.size == 0:
            return self.append(item)
        else:
            self.head.next = LinkedNode(item)
            self.head = self.head.next
            self.head.next = self.tail
        self.size += 1

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

    def rem(self, item):
        return self.RemoveFirst(item)

    def mergeSort(self, **kwargs):
        return super(CircularLinkedList, self).mergeSort(isCircular=True)