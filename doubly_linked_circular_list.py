from doubly_linked_list import DoublyLinkedNode, DoublyLinkedList


class CircularDoublyLinkedList(DoublyLinkedList):
    def __getattribute__(self, item):
        # TODO test anyway
        item = super().__getattribute__(item)
        if callable(item):
            def ret(*args, **kwargs):
                item(*args, **kwargs)
                if len(self) > 0:
                    self.tail.next = self.head
                    self.head.prev = self.tail
            return ret
        else:
            return item

    def __str__(self):
        #start breaks on console but it shoudl work on the terminal
        return "... <-> " + str(self.tail) + " <-> " + super().__str__() + " <-> " + str(self.head) + " <-> ..."


if __name__ == "__main__":
    print("Local tests")

