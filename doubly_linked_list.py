from typing import Literal, Tuple, List

from base_classes import LinkedNode, LinkedList


# TODO: I really don't know how to implement Nota 2
class DoublyLinkedNode(LinkedNode):
    def __init__(self, value, next=None, prev=None):
        super().__init__(value, next)
        self.prev: DoublyLinkedNode | None = prev

    def move_n_times_left(self, n):
        current_node = self
        for i in range(n):
            if current_node.prev is None:
                raise DoublyLinkedNode.NoPrev("Index out of range")
            current_node = current_node.prev
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

    def popLink(self):
        self.prev = self.next

    def getAllLeft(self):
        left = self.prev
        while left is not None:
            yield left
            left = left.prev
    def disconect(self):
        A = self.prev, B = self, C = self.next
        if A is not None: A.next = C
        if C is not None: C.prev = A

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

    def append(self, value):
        if self.size == 0:
            self.head = DoublyLinkedNode(value)
            self.tail = self.head
        else:
            self.tail.next = DoublyLinkedNode(value, prev=self.tail)
            self.tail = self.tail.next
        self.size += 1

    def prepend(self, value):
        if self.size == 0:
            self.head = DoublyLinkedNode(value)
            self.tail = self.head
        else:
            self.head = DoublyLinkedNode(value, next=self.head)
            self.head.prev = self.head

    def ins(self, item):
        return self.append(item)

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
                i.disconnect()
                self.size -= 1

    def rem(self, value):
        return self.removeFirst(value)

    def findMiddle(self, startPoint : Tuple[DoublyLinkedNode, int] = None, endPoint : Tuple[DoublyLinkedNode, int] = None)-> Tuple[DoublyLinkedNode, int]:
        #TODO test
        #if range count is even then there are 2 middle nodes, this gets the first one
        if startPoint is None: startPoint = (self.head, 0)
        if endPoint is None: endPoint = (self.tail, self.size - 1)
        count = startPoint[1]-endPoint[1]
        if count % 2 == 0:
            #Test this specifically too
            return startPoint[0].move_n_times_right(count // 2 - 1), (count // 2 - 1) + startPoint[1]
        else:
            return startPoint[0].move_n_times_right(count // 2), (count // 2) + startPoint[1] # TODO check

    def binarySearch(self, item, order=False) -> Tuple[DoublyLinkedNode, int]:  # TODO change to True default
        if order:
            self.ordenar()
        start = (self.head, 0)
        end = (self.tail, self.size-1)
        mid = self.findMiddle(start, end)
        if mid[0].value == item:
            return mid
        elif mid[0].value > item:
            start = (mid[0].next, mid[1] + 1)
        else:
            end = (mid[0].prev, mid[1] - 1)
        #todo

    def insertionSort(self):
        # TODO test this ty
        listLen = len(self)
        if listLen in [0, 1]:
            return
        for current_node in self:
            if current_node.value > current_node.next.value:
                nodePopped: DoublyLinkedNode = current_node.next
                valueOfPoppedNode = nodePopped.value
                nodePopped.popLink()
                del nodePopped
                nodeWithValueLessThanPopped: DoublyLinkedNode | None = None
                for nodeLeftToPopped in current_node.getAllLeft():
                    if nodeLeftToPopped.value < valueOfPoppedNode:
                        nodeWithValueLessThanPopped = nodeLeftToPopped
                        break
                if nodeWithValueLessThanPopped is None:
                    self.prepend(valueOfPoppedNode)
                nodeWithValueLessThanPopped.insertNext(valueOfPoppedNode)
        self.tail = current_node  # will always exist because listLen can't be 0

    def bubbleSort(self):
        # TODO test it ty
        is_sorted = False
        lastOrdered = None
        while not is_sorted:
            is_sorted = True
            current_node = self.head
            while current_node.next is not None or current_node.next != lastOrdered:
                if current_node.value > current_node.next.value:
                    DoublyLinkedNode.swap(current_node, current_node.next)
                    is_sorted = False
                    lastOrdered = current_node.next.value
                current_node = current_node.next

    def ordenar(self, which: Literal['m', 'q', 'i', 'b'] = "m"):  # TODO mudar para o mais efetivo
        return super().ordenar(which)


if __name__ == "__main__":
    pass

# tests TODO
dll1 = DoublyLinkedList()
lista_norm = [1, 2, 3, 4]# any possible list
valor = 3# value
indice = 2# index (begins on 0)
# test functions
def appendtest(lista_normal):
    lista_comp = []
    global app_test_result
    app_test_result = False

    for element_norm in lista_normal:
        dll1.append(element_norm)

    for node in dll1:
        lista_comp.append(node.value)

    if lista_comp == lista_normal:
        app_test_result = True

    return app_test_result

#se a lista ligada é igual à normal em conteúdo
def lentest():
    if app_test_result:
        return len(lista_norm) == dll1.len() == len(dll1)
    return False

def mostrartest():
    if not app_test_result:# it is essencial to guarantee that the linked list is equal to the test python list
        # we are comparing it to
        return False

    lst1 = ' <-> '.join([str(element_norm) for element_norm in lista_norm])
    lst2 = dll1.__str__()
    return lst1 == lst2

#this function searches for a certain value. It returns 0 if the value is not on the linked list,
#otherwise it will return the position of the first element of the linkedlist that equals the given value
def existetest(vlr):
    if not app_test_result:
        return False

    lst_string = ''
    for elemento in lista_norm:
        lst_string += str(elemento)

    return lst_string.find(str(vlr)) + 1 == dll1.existe(vlr)

def vertest(ind):
    if not app_test_result:
        return False

    if ind >= len(lista_norm) or ind < 0:
        raise IndexError("Índice inválido")

    return lista_norm[ind] == dll1.ver(ind)

#def remtest(vlr):
    #lista_comp2 = []

    #if not app_test_result:
        #return False

    #dll1.rem(vlr)
    #for node in dll1:
        #lista_comp2.append(node.value)

    #return lista_norm.remove(vlr) == lista_comp2

def limpartest():
    lista_norm = []
    dll1.limpar()
    return len(lista_norm) == dll1.len() == len(dll1) == 0

def vaziatest():
    if limpartest():
        return True
    return False





test = {'ins(item)': appendtest(lista_norm), 'len()': lentest(), 'mostrar()': mostrartest(),
        'existe(item)': existetest(valor), 'ver(p)': vertest(indice), 'ordenar()': '?', 'rem(item)': '?'
    , 'limpar()': limpartest(), 'vazia()': vaziatest()}

for i in test:
    print(f'{i} --> {test[i]}')


