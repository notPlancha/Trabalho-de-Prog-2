import warnings
from typing import Literal, Tuple, List

from base_classes import LinkedNode, LinkedList


class DoublyLinkedNode(LinkedNode):
    def __init__(self, value, next=None, prev=None):
        super(DoublyLinkedNode, self).__init__(value, next)
        self.prev: DoublyLinkedNode | None = prev

    def move_n_times_left(self, n):
        current_node = self
        for i in range(n):
            if current_node.prev is None:
                raise DoublyLinkedNode.NoPrev("Index out of range")
            current_node = current_node.prev
        return current_node

    class NoPrev(IndexError):
        pass

    def represent(self, arrows_left=False, arrows_right=False):
        h = str(self)
        if arrows_left:
            h = "<->" + h
        if arrows_right:
            h = h + "<->"
        return h

    def move_link_right(self):
        if self.next is None:
            raise DoublyLinkedNode.NoNext("Index out of range")
        DoublyLinkedNode.swap(self, self.next)

    def move_link_left(self):
        if self.prev is None:
            raise DoublyLinkedNode.NoPrev("Index out of range")
        DoublyLinkedNode.swap(self, self.prev)

    def insertNext(self, value, listWarning=True):
        if listWarning: warnings.warn(
            "InsertNext should not be used for linkedList manipulation unless used with caution")
        nod = DoublyLinkedNode(value, next=self.next, prev=self)
        if nod.next is not None:
            nod.next.prev = nod
        self.next = nod
        return nod

    def insertPrev(self, value, listWarning=True):
        if listWarning: warnings.warn(
            "InsertNext should not be used for linkedList manipulation unless used with caution")
        nod = DoublyLinkedNode(value, next=self, prev=self.prev)
        if nod.prev is not None:
            nod.prev.next = nod
        self.prev = nod
        return nod

    def getAllLeft(self):
        left = self.prev
        while left is not None:
            yield left
            left = left.prev

    def disconect(self):
        A = self.prev
        C = self.next
        if A is not None: A.next = C
        if C is not None: C.prev = A


class DoublyLinkedList(LinkedList):  # noqa
    def __getitem__(self, p):
        if p >= 0:
            return super(DoublyLinkedList, self).__getitem__(p)
        else:
            if -p > self.size:
                raise IndexError("Index out of range")
            else:
                return self.tail.move_n_times_left(-p - 1)

    def __str__(self):
        if self.head is None:
            return 'Empty'
        return " <-> ".join([str(node) for node in self])

    def append(self, value):
        if self.size == 0:
            self.head = DoublyLinkedNode(value)
            self.tail = self.head
        else:
            self.tail.next = DoublyLinkedNode(value, prev=self.tail)
            self.tail = self.tail.next
        self.size += 1

    def prepend(self, value):
        if self.size == 0:
            self.head = DoublyLinkedNode(value)
            self.tail = self.head
        else:
            self.head = DoublyLinkedNode(value, next=self.head)
            self.head.next.prev = self.head

    def ins(self, item):
        return self.append(item)

    def first(self, value) -> DoublyLinkedNode | None:
        return super(DoublyLinkedList, self).first(value)

    # true if it found one
    def removeFirst(self, value) -> bool:
        if self.first(value) is None:
            if self.head == value:
                return self.limpar()
            return False

        NodeOfValue: DoublyLinkedNode = self.first(value)
        Prev = NodeOfValue.prev
        Next = NodeOfValue.next

        if len(self) == 2:
            if Prev is None:
                self.head = Next
                self.tail = self.head
            if Next is None:
                self.tail = Prev
                self.head = self.tail

            NodeOfValue.disconect()
            self.size -= 1
            return True

        elif NodeOfValue is not None:
            if Prev is None:
                self.head = Next

            if Next is None:
                self.tail = Prev

            NodeOfValue.disconect()
            self.size -= 1
            return True

        else:
            return False

    def removeAll(self, value):
        # removes all of value
        while self.rem(value) is False:
            continue
        return

    def rem(self, value):
        return self.removeFirst(value)

    @staticmethod
    def sortedMerge(a, b) -> Tuple[LinkedNode, LinkedNode, int]:
        pointera = a.head
        pointerb = b.head
        retHead = currentNode = DoublyLinkedNode(0)
        while True:
            if pointera.value > pointerb.value:
                pointera, pointerb = pointerb, pointera
                a, b = b, a
            currentNode = currentNode.insertNext(pointera.value, listWarning=False)
            if pointera.next is None or pointera is a.tail:
                for i in pointerb:
                    currentNode = currentNode.insertNext(i.value, listWarning=False)
                    if i is b.tail:
                        break
                return retHead.next, currentNode, a.size + b.size
            else:
                pointera = pointera.next


if __name__ == "__main__":
    from Testes_ao_codigo import fromListToDll

    dll = fromListToDll([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    print(dll.binarySearch(5))
