from base_classes import LinkedNode, LinkedList


# TODO: I really don't know how to implement Nota 2

# TODO: add binary search(both methods?)
class CircularLinkedList(LinkedList): # noqa
    def __init__(self, head=None, tail=None):
        super().__init__(head)
        self.tail: LinkedNode | None = tail

    def __str__(self):
        return super().__str__() + " -> " + str(self.head) + "-> ..."

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
            if i.data == item:
                if prev is None:
                    # data is in head
                    self.head = self.head.next
                    self.tail.next = self.head
                else:
                    prev.next = i.next
                return True
            prev = i
        return False

    def ordenar(self, mode = ""):
        # TODO test pls
        if self.size == 0:
            return
        if mode == "i":
            current_node = self.head
            for i in range(self.size):
                for j in range(self.size - 1):
                    if current_node.data > current_node.next.data:
                        current_node.data, current_node.next.data = current_node.next.data, current_node.data
                    current_node = current_node.next
                current_node = self.head
            self.tail = current_node
            assert self.tail.next == self.head
            self.tail.next = self.head
        if mode == "b":
            for j in range(self.len - 1):
                for i in range(self.len -1):
                    if self[i] > self[i+1]:
                        self[i], self[i+1] = self[i+1], self[i]


if __name__ == "__main__":
    # tests TODO
    pass
