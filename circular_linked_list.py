import warnings
from typing import Literal, Tuple

from base_classes import LinkedNode, LinkedList


# TODO: I really don't know how to implement Nota 2

class CircularLinkedList(LinkedList):  # noqa
    def __str__(self):
        return super().__str__() + " -> " + str(self.head) + "-> ..."

    def ordenar(self, which: Literal['m', 'q', 'i', 'b'] = "m"):  # TODO mudar para o mais efetivo
        return super().ordenar(which)

    def append(self, item):
        if self.size == 0:
            self.head = LinkedNode(item)
            self.tail = self.head
            self.head.next = self.head
        else:
            self.tail.next = LinkedNode(item)
            self.tail = self.tail.next
            self.tail.next = self.head
        self.size += 1

    def prepend(self, item):
        if self.size == 0:
            return self.append(item)
        else:
            self.head.next = LinkedNode(item)
            self.head = self.head.next
            self.head.next = self.tail
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
                return True
            prev = i
        return False

    def bubbleSort(self):
        # TODO Test here too
        is_sorted = False
        lastOrdered = None
        while not is_sorted:
            is_sorted = True
            current_node = self.head
            while current_node.next is not None or current_node.next != lastOrdered:
                if current_node.value > current_node.next.value:
                    LinkedNode.swap(current_node, current_node.next)
                    is_sorted = False
                    lastOrdered = current_node.next.value
                current_node = current_node.next

    def binarySearch(self, item, order=False) -> Tuple[LinkedNode | None, int]:  # TODO change to True default
        # TODO test it ty
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

    def binarySearchOld(self, item):
        # TODO remove it ?
        warnings.warn("use binarySearch Instead", DeprecationWarning)
        listlen = (len(self) // 2)
        for i in range(listlen, len(self)):
            m = self.head.move_n_times_rigth(self, listlen)
            if m.value == item:
                return index(m)
            if m.value < item:
                m = self[index(m) + m // 2]
            if item < m.value:
                m = self[index(m) // 2]
            return 0

    def insertionSort(self):
        listLen = len(self)
        if listLen in [0, 1]:
            return
        current_node = None
        prev = None
        for current_node in self:
            if current_node.value > current_node.next.value:
                nodePopped: LinkedNode = current_node.next
                valueOfPoppedNode = nodePopped.value
                if prev is not None: prev.next = nodePopped.next
                del nodePopped
                nodeWithValueLessThanPopped: LinkedNode | None = None
                for nodeLeftToPopped in current_node.getAllLeft():
                    if nodeLeftToPopped.value < valueOfPoppedNode:
                        nodeWithValueLessThanPopped: LinkedNode | None = nodeLeftToPopped
                        break
                if nodeWithValueLessThanPopped is None:
                    self.prepend(valueOfPoppedNode)
                else:
                    nodeWithValueLessThanPopped.insertNext(valueOfPoppedNode)
                prev = current_node
        self.tail = current_node  # will always exist because listLen can't be 0

    # noinspection PyUnreachableCode
    def insertionSortOld(self):
        raise NotImplementedError("use insertionSort instead")
        # TODO current implementation will never work
        """
        for i in range(1, self.size):
            aux = self.head.move_n_times_rigth(i)
            j = i - 1
            while j >= 0 and self[j] > aux:
                self.head.move_n_times_rigth(j + 1) = self.head.move_n_times_rigth(j)
                j = j - 1
        """


if __name__ == "__main__":
    # tests TODO
    node1 = LinkedNode(7)
    node1.insertNext(5)
    print(node1)
    print(node1.next)
