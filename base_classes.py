# base classes of linked lists should not have remove and insert methods (and binary search)
import warnings
from typing import Literal, Tuple, List


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
        current_node : LinkedNode = self
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

    def insertNext(self, value, listWarning = True):
        if listWarning: warnings.warn("InsertNext should not be used for linkedList manipulation unless used with caution")
        self.next = LinkedNode(value, self.next)
        return self.next

    def __iter__(self):
        currentNode = self
        while currentNode is not None:
            yield currentNode
            currentNode = currentNode.next
        raise StopIteration
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __iter__(self) -> LinkedNode:
        if self.size <= 1:
            return iter([self.head])
        current_node = self.head
        while current_node is not self.tail and current_node is not None:
            yield current_node
            current_node = current_node.next
        yield self.tail

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
        if len(self) == 0:
            return 'Empty'

        if len(self) == 1:
            return f'{self.head.value}'
        else:
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

    @staticmethod
    def sortedMerge(a,b, isDoublyLinked = False) -> Tuple[LinkedNode, LinkedNode, int]:
        #TODO test
        pointera = a.head
        pointerb = b.head
        retHead = currentNode = LinkedNode(0)
        while True:
            if pointera.value > pointerb.value:
                currentNode = currentNode.insertNext(pointera.value, listWarning=False)
                if pointera.next is None:
                    for i in pointerb:
                        currentNode = currentNode.insertNext(i.value)
                    return retHead.next, currentNode, a.size + b.size
                else:
                    pointera = pointera.next
            else:
                currentNode = currentNode.insertNext(pointerb.value, listWarning=False)
                if pointerb.next is None:
                    for i in pointera:
                        currentNode = currentNode.insertNext(i.value, listWarning=False)
                    return retHead.next, currentNode, a.size + b.size
    def mergeSort(self, isCircular = False, isDoublyLinked = False):
        #TODO test e verifiar se é preciso os trues e falses
        if isCircular: #verificar se é preciso
            self.tail = None
        if self.size == 1:
            return
        mid = self.findMiddle()
        a = type(self)()
        a.head = self.head
        a.tail = mid[0]
        a.size = mid[1] + 1
        b = type(self)()
        b.head = mid[0].next
        b.tail = self.tail
        b.size = self.size - mid[1]

        a.mergeSort()
        b.mergeSort()

        result = type(self).sortedMerge(a, b)
        self.head = result[0]
        self.tail = result[1]
        self.size = result[2]
        if isCircular: # verificar se é preciso
            self.tail.next = self.head

    def quickSort(self):
        raise NotImplementedError("quickSort not implemented on this list")

    def insertionSort(self):
        raise NotImplementedError("insertionSort not implemented on this list")

    def bubbleSort(self):
        is_sorted = False
        while not is_sorted:
            is_sorted = True
            current_node = self.head
            while current_node.next is not None:
                if current_node.value > current_node.next.value:
                    LinkedNode.swap(current_node, current_node.next)
                    is_sorted = False
                current_node = current_node.next

    def indexOf(self, value) -> int:
        a = 0
        for i in self:
            if i.value == value:
                return a
            a += 1
        return -1

    def existe(self, value) -> int:
        return self.indexOf(value) + 1

    def findMiddle(self, startPoint: Tuple[LinkedNode, int] = None,
                   endPoint: Tuple[LinkedNode, int] = None) -> Tuple[LinkedNode, int]:
        # TODO test
        if startPoint is None: startPoint = (self.head, 0)
        if endPoint is None: endPoint = (self.tail, self.size - 1)
        count = endPoint[1] - startPoint[1]
        return [startPoint[0].move_n_times_right(count // 2), (count // 2) + startPoint[1]]  # TODO check

    def findMiddleNode(self, startNode = None):
        warnings.warn("Depricated, use findMiddle Instead")
        if len(self) == 0:
            return None

        if startNode is None:
            startNode = self.head

        slow = fast = startNode

        while (fast.next is not None) and (fast.next.next is not None):
            slow = slow.next
            fast = fast.next.next
        return slow
