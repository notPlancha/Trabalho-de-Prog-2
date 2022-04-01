class SinglyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def len(self):
        return len(self)

    def vazia(self):
        return self.size == 0

    def limpar(self):
        self.__init__()

    def insert_first(self, data):
        new_node = SinglyLinkedNode(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def ins(self, data, index):
        if index < 0 or index > self.size:
            raise IndexError('Índice inválido')
        if index == 0:
            self.insert_first(data)
        else:
            new_node = SinglyLinkedNode(data)
            current_node = self.head
            for i in range(index - 1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
            self.size += 1

    def remove_first(self):
        if self.size == 0:
            raise IndexError('Lista vazia')
        self.size -= 1
        if self.size == 0:
            self.limpar()
        self.head = self.head.next
        self.tail.next = self.head

    def rem(self, index):
        if index < 0 or index >= self.size:
            raise IndexError('Índice inválido')
        if index == 0:
            self.remove_first()
        else:
            current_node = self.head
            for i in range(index - 1):
                current_node = current_node.next
            current_node.next = current_node.next.next
            self.size -= 1
            if index == self.size:
                self.tail = current_node
    def __str__(self):
        if self.size == 0:
            return 'Lista vazia'
        current_node = self.head
        string = ''
        for i in range(self.size):
            string += str(current_node.data)
            if i == self.tail:
                string += "->" + str(self.head.data) + "-> ..."
            else:
                string += "->"
            current_node = current_node.next
        return string
    def mostrar(self):
        print(self)

class SinglyLinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None
