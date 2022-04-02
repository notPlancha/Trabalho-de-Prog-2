class SinglyCircularLinkedList:
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

    def ver(self, p):
        if p < 0 or p >= self.size:
            raise IndexError('Índice inválido')
        current_node = self.head
        for i in range(p):
            current_node = current_node.next
        return current_node.data

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

    def insert_on_index(self, data, index):
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

    def rem_on_index(self, index):
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

    def existe(self, item):
        current_node = self.head
        for i in range(self.size):
            if current_node.data == item:
                return True
            current_node = current_node.next
        return False

    # insert last
    def ins(self, item):
        self.insert_on_index(item, self.size)

    # remove item
    def rem(self, item):
        if item == self.head.data:
            self.remove_first()
            return
        current_node = self.head
        while current_node.next is not None and current_node.next.data != item:
            current_node = current_node.next
        if current_node.next is None:
            raise ValueError('Item não encontrado')
        else:
            if current_node.next == self.tail:
                self.tail = current_node
            current_node.next = current_node.next.next
        self.size -= 1

    def ordenar(self):
        if self.size == 0:
            return
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


class SinglyLinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    def move_n_times(self, n):
        current_node = self
        for i in range(n):
            current_node = current_node.next
        return current_node


if __name__ == "__main__":
    # tests
    pass
