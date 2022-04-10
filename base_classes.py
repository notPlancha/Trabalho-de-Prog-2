# base classes of linked lists should not have remove and insert methods (and binary search)
from typing import Literal


class LinkedNode:

    @staticmethod
    def swap(node1, node2):
        node1.value, node2.value = node2.value, node1.value

    def __init__(self, value, next=None):
        self.value = value
        self.next: LinkedNode | None = next

    class NoNext(IndexError):
        pass

    def __eq__(self, other):
        if other is None: return False
        elif isinstance(other, LinkedNode): return self.value == other.value
        else: return self.value == other

    def move_n_times_right(self, n):
        current_node = self
        for i in range(n):
            if current_node.next is None:
                raise LinkedNode.NoNext("Index out of range")
            current_node = current_node.next
        return current_node

    def __str__(self):
        return str(self.value)

    def represent(self, arrows=False):
        if not arrows:
            return str(self)
        else:
            return f"{self.value} ->"

    def insertNext(self, value):
        #TODO test ty
        self.next = LinkedNode(value, self.next)
        return self.next

class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def __iter__(self) -> LinkedNode:
        current_node = self.head
        while current_node is not None:
            yield current_node
            current_node = current_node.next

    def __getitem__(self, p):
        if p >= self.size or p < 0:
            raise IndexError("Índice inválido")
        else:
            return self.head.move_n_times_right(p)

    def __len__(self):
        return self.size

    def len(self):
        return len(self)

    def vazia(self):
        return self.size == 0

    def limpar(self):
        self.__init__()

    def mostrar(self):
        print(self)

    def __str__(self):
        return " -> ".join([str(node) for node in self])

    def ver(self, p):
        return self[p].value

    def first(self, value) -> LinkedNode | None:
        for i in self:
            if i.value == value:
                return i
        return None

    def all(self, value) -> [LinkedNode]:
        ret = []
        for i in self:
            if i.value == value:
                ret.append(i)
        return ret

    # sort a linkedList
    def ordenar(self, which: Literal['m', 'q', 'i', 'b']):
        if which == 'm':
            self.mergeSort()
        elif which == 'q':
            self.quickSort()
        elif which == 'i':
            self.insertionSort()
        elif which == 'b':
            self.bubbleSort()
        else:
            raise ValueError("Invalid argument")

    def mergeSort(self):
        raise NotImplementedError("mergeSort not implemented on this list")

    def quickSort(self):
        raise NotImplementedError("quickSort not implemented on this list")

    def insertionSort(self):
        raise NotImplementedError("insertionSort not implemented on this list")

    def bubbleSort(self):
        raise NotImplementedError("bubbleSort not implemented on this list")

    def indexOf(self, value) -> int:
        a = 0
        for i in self:
            if i.value == value:
                return a
            a += 1
        return -1

    def existe(self, value) -> int:
        return self.indexOf(value) + 1