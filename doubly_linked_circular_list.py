from doubly_linked_list import DoublyLinkedNode, DoublyLinkedList

class CircularDoublyLinkedList(DoublyLinkedList):
    def __getattribute__(self, item):
        item = super(CircularDoublyLinkedList, self).__getattribute__(item)
        if callable(item):
            def ret(*args, **kwargs):
                item(*args, **kwargs)
                self.tail.next = self.head
            return ret
        else:
            return item