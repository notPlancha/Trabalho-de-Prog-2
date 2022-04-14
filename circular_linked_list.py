from typing import Literal

from base_classes import LinkedNode, LinkedList


# TODO: I really don't know how to implement Nota 2

class CircularLinkedList(LinkedList): # noqa
    def __init__(self, head=None, tail=None):
        super().__init__(head)
        self.tail: LinkedNode | None = tail

    def __str__(self):
        return super().__str__() + " -> " + str(self.head) + "-> ..."

    def ordenar(self, which: Literal['m', 'q', 'i', 'b'] = "m"): #TODO mudar para o mais efetivo
        return super().ordenar(which)
    # append to the list
    def ins(self, item):
        if self.size == 0:
            self.head = LinkedNode(item)
            self.tail = self.head
            self.head.next = self.head
        else:
            self.tail.next = LinkedNode(item)
            self.tail = self.tail.next
            self.tail.next = self.head
        self.size += 1

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
        pass

    def binarySearch(self, item):
        #TODO
        listlen = (len(self)//2)
        for i in range(listlen, len(self)):
            m = self.head.move_n_times_rigth(self, listlen)
            if m.value == item:
                return index(m)
            if m.value < item:
                m = self[index(m) + m//2]
            if item < m.value:
                m = self[index(m)//2]
            return 0

    def insertionSort(self):
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