from typing import Literal, Tuple, List

from base_classes import LinkedNode, LinkedList


# TODO: I really don't know how to implement Nota 2
class DoublyLinkedNode(LinkedNode):
    def __init__(self, value, next=None, prev=None):
        super().__init__(value, next)
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

    def insertNext(self, value):
        # TODO test ty
        nod = DoublyLinkedNode(value, next=self.next, prev=self)
        if nod.next is not None:
            nod.next.prev = nod
        self.next = nod
        return nod

    def insertPrev(self, value):
        # TODO test ty
        nod = DoublyLinkedNode(value, next=self, prev=self.prev)
        if nod.prev is not None:
            nod.prev.next = nod
        self.prev = nod
        return nod

    def popLink(self):
        self.prev = self.next

    def getAllLeft(self):
        left = self.prev
        while left is not None:
            yield left
            left = left.prev

    def disconect(self, B_prev_node, B_next_node):
        A = B_prev_node
        C = B_next_node
        if A is not None: A.next = C
        if C is not None: C.prev = A

class DoublyLinkedList(LinkedList):  # noqa
    def __getitem__(self, p):
        if p >= 0:
            return super().__getitem__(p)
        else:
            if -p > self.size:
                raise IndexError("Index out of range")
            else:
                return self.tail.move_n_times_left(-p - 1)

    def __str__(self):
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
            self.head.prev = self.head

    def ins(self, item):
        return self.append(item)

    def first(self, value) -> DoublyLinkedNode | None:
        return super().first(value)

    # true if it found one
    def removeFirst(self, value) -> bool:
        if self.first(value) is None:
            if self.head == value:
                return self.limpar()
            return False

        NodeOfValue = self.first(value)
        Prev = NodeOfValue.prev
        Next = NodeOfValue.next

        if len(self) == 2:
            if Prev is None:
                self.head = Next
                self.tail = self.head
            if Next is None:
                self.tail = Prev
                self.head = self.tail

            NodeOfValue.disconect(Prev, Next)
            self.size -= 1
            return

        elif NodeOfValue is not None:
            if Prev is None:
                self.head = Next

            if Next is None:
                self.tail = Prev

            NodeOfValue.disconect(Prev, Next)
            self.size -= 1
            return

        else:
            return False

    def removeAll(self, value):
        while self.rem(value) != False:
            continue
        return

    def rem(self, value):
        return self.removeFirst(value)

    def binarySearch(self, item, order=False) -> Tuple[DoublyLinkedNode | None, int]:  # TODO change to True default
        #TODO test it ty
        if order:
            self.ordenar()
        start = (self.head, 0)
        end = (self.tail, self.size-1)
        while end[0] != start[0] or end[0] is None or start[0] is None: #not sure of this line
            mid = self.findMiddle(start, end)
            if mid[0].value == item:
                return mid
            elif mid[0].value > item:
                start = (mid[0].next, mid[1] + 1)
            else:
                end = (mid[0].prev, mid[1] - 1)
        return None, -1

    def insertionSort(self):
        # TODO test this ty
        listLen = len(self)
        if listLen in [0, 1]:
            return
        current_node = None
        for current_node in self:
            if current_node.value > current_node.next.value:
                nodePopped: DoublyLinkedNode = current_node.next
                valueOfPoppedNode = nodePopped.value
                nodePopped.popLink()
                del nodePopped
                nodeWithValueLessThanPopped: DoublyLinkedNode | None = None
                for nodeLeftToPopped in current_node.getAllLeft():
                    if nodeLeftToPopped.value < valueOfPoppedNode:
                        nodeWithValueLessThanPopped = nodeLeftToPopped
                        break
                if nodeWithValueLessThanPopped is None:
                    self.prepend(valueOfPoppedNode)
                else:
                    nodeWithValueLessThanPopped.insertNext(valueOfPoppedNode)
        self.tail = current_node  # will always exist because listLen can't be 0

# BubbleSort by swaping node values that are adjacent to each
    def bubbleSortNew(self):
        is_sorted = True

        for i in range(len(self) - 1):
            if self[i].value > self[i + 1].value:
                DoublyLinkedNode.swap(self[i], self[i + 1])
                is_sorted = False
            continue

        if is_sorted:
            return

        else:
            self.bubbleSortNew()

    def bubbleSort(self):
        # TODO test it ty
        is_sorted = False
        lastOrdered = None
        while not is_sorted:
            is_sorted = True
            current_node = self.head
            while current_node.next is not None or current_node.next != lastOrdered:
                if current_node.value > current_node.next.value:
                    DoublyLinkedNode.swap(current_node, current_node.next)
                    is_sorted = False
                    lastOrdered = current_node.next.value
                current_node = current_node.next

    def ordenar(self, which: Literal['m', 'q', 'i', 'b'] = "m"):  # TODO mudar para o mais efetivo
        return super().ordenar(which)

if __name__ == "__main__": #TODO remove this from final
    print("Local tests")
