from doubly_linked_list import DoublyLinkedNode, DoublyLinkedList

class CircularDoublyLinkedList(DoublyLinkedList):
    def __getattribute__(self, item):
        #TODO test anyway
        item = super().__getattribute__(item)
        if callable(item):
            def ret(*args, **kwargs):
                item(*args, **kwargs)
                self.tail.next = self.head
                self.head.prev = self.tail
            return ret
        else:
            return item
    def ver(self):
        #TODO
        pass
if __name__ == "__main__":
    pass