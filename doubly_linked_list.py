class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node.data
            current_node = current_node.next

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
        if self.size == 0:
            return 'Lista vazia'
        current_node = self.head
        string = ''
        for i in range(self.size):
            string += str(current_node.data)
            if i == self.tail:
                string += "<->" + str(self.head.data) + "<-> ..."
            else:
                string += "<->"
            current_node = current_node.next
        return string



class DoublyLinkedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev
