from base_classes import LinkedNode, LinkedList


# TODO: I really don't know how to implement Nota 2

# TODO: add binary search (both methods?)
class DoublyLinkedNode(LinkedNode):
    def __init__(self, value, next=None, prev=None):
        super().__init__(value, next)
        self.prev: DoublyLinkedNode | None = prev

    def move_n_times_left(self, n):
        current_node = self
        for i in range(n):
            if type(current_node) is DoublyLinkedNode:
                current_node = current_node.prev
            else:
                raise DoublyLinkedNode.NoPrev("Index out of range")
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


class DoublyLinkedList(LinkedList):  # noqa
    def __init__(self, head=None, tail=None):
        super().__init__(head)
        self.tail: DoublyLinkedNode | None = tail

    def __getitem__(self, p):
        if p > 0:
            return super().__getitem__(p)
        else:
            if -p > self.size:
                raise IndexError("Index out of range")
            else:
                return self.tail.move_n_times_left(-p - 1)

    def __str__(self):
        return " <-> ".join([str(node) for node in self])

    # append to the list
    def ins(self, item):
        if self.size == 0:
            self.head = DoublyLinkedNode(item)
            self.tail = self.head
        else:
            self.tail.next = DoublyLinkedNode(item, prev=self.tail)
            self.tail = self.tail.next
        self.size += 1

    def removeNode(self, node: LinkedNode):
        node.prev = node.next
        self.size -= 1

    # true if it found one
    def removeFirst(self, value) -> bool:
        NodeOfValue = self.first(value)
        if NodeOfValue is not None:
            self.removeNode(NodeOfValue)
            self.size -= 1
            return True
        else:
            return False

    def removeAll(self, value):
        for i in self:
            if i.value == value:
                self.removeNode(i)
                self.size -= 1

    def rem(self, value):
        return self.removeFirst(value)

    def insertionSort(self):
        if self.size == 0:
            return
        current_node = self.head
        while current_node is not None:
            while current_node.prev is not None:
                if current_node.value < current_node.prev.value:
                    current_node.move_link_left()
                else:
                    break
            current_node = current_node.next


if __name__ == "__main__":
    # tests TODO
    pass
