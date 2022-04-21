from typing import Literal

from doubly_linked_list import DoublyLinkedList, DoublyLinkedNode
from circular_linked_list import CircularLinkedList
from base_classes import LinkedNode

#Objects and variables that will be used specifically on this test (can be changed)
lst_norm = [1, 2, 3, 4]# list
vlr = 3# value
ind = 2# index (begins on 0)

def fromListToDll(lista_normal) -> DoublyLinkedList:
    if len(lista_normal) == 0:
        return DoublyLinkedList()
    elif len(lista_normal) == 1:
        ret = DoublyLinkedList()
        ret.head = ret.tail = DoublyLinkedNode(lista_normal[0])
        ret.size += 1
        return ret
    first = prev = DoublyLinkedNode(lista_normal[0])
    for i in lista_normal[1:]:
        curr = DoublyLinkedNode(i)
        curr.prev = prev
        prev.next = curr
        prev = curr
    ret = DoublyLinkedList()
    ret.head = first
    ret.tail = prev
    ret.size = len(lista_normal)
    return ret

def fromDllToList(dll):
    current_node = dll.head
    ret = []
    while current_node is not None:
        ret.append(current_node.value)
        current_node = current_node.next
    return ret

def fromListToCll(lista_normal) -> CircularLinkedList:
    ret = CircularLinkedList()
    if len(lista_normal) == 0:
        return ret

    if len(lista_normal) == 1:
        ret.head = ret.tail = LinkedNode(lista_normal[0])
        ret.size = 1
        ret.head.next = ret.tail
        return ret

    ret.head = current_node = LinkedNode(lista_normal[0])
    for elem in lista_normal[1:]:
        current_node.next = current_node = LinkedNode(elem)

    ret.tail = current_node
    ret.tail.next = ret.head
    ret.size = len(lista_normal)
    return ret

# test functions
def insTest(lista_normal):
    lista_comp = []
    lista_comp_rev = []
    dll1 = DoublyLinkedList()

    for element_norm in lista_normal:
        dll1.ins(element_norm)

    current_node = dll1.head
    while current_node is not None:
        lista_comp.append(current_node.value)
        current_node = current_node.next

    current_node = dll1.tail
    while current_node is not None:
        lista_comp_rev.append(current_node.value)
        current_node = current_node.prev

    lista_comp_rev.reverse()
    return lista_comp == lista_comp_rev == lista_normal

def lenTest(lista_normal):
    dll1 = fromListToDll(lista_normal)
    return len(lista_normal) == len(dll1) == dll1.len() == dll1.size

def mostrarTest(lista_normal):
    dll1 = fromListToDll(lista_normal)
    lst1 = ' <-> '.join([str(element_norm) for element_norm in lista_normal])
    dll1.mostrar()
    return (print(lst1) == dll1.mostrar())

#this function searches for a certain value. It returns 0 if the value is not on the linked list,
#otherwise it will return the position of the first element of the linkedlist that equals the given value
def existeTest(lista_normal):
    dll1 = fromListToDll(lista_normal)
    lst_string = ''

    for elemento in lista_normal:
        lst_string += str(elemento)

    for valor in lst_string:
        if (lst_string.find(valor) + 1 == dll1.existe(int(valor))) is not True:
            return False
    return True

def verTest(lista_normal, indice):
    dll1 = fromListToDll(lista_normal)

    try:
        value = lista_normal[indice]
    except IndexError:
        try:
            dll1.ver(indice)
            return False
        except:
            return False

    try:
        value2 = dll1.ver(indice)
        return value == value2
    except:
        return False

def remTest(lista_normal, item):
    dll1 = fromListToDll(lista_normal)
    dll1 = dll1.rem(item)
    lista_normal = lista_normal.remove(item)

    if dll1 == False:
        return False

    dll1 = fromDllToList(dll1)
    return dll1 == lista_normal

def limparTest(lista_normal):
    dll1 = fromListToDll(lista_normal)

    dll1.limpar()

    lista_comp = fromDllToList(dll1)

    return lista_comp == []

def vaziaTest(lista_normal):
    dll1 = fromListToDll(lista_normal)
    lst1 = fromDllToList(dll1)

    dll2 = DoublyLinkedList()
    return (dll1.vazia() == (len(lst1) == 0)) and (dll2.vazia())

def ordenarTest(lista_normal, sortMethod : Literal['m', 'q', 'i', 'b'] = 'b'):
    dll1 = fromListToDll(lista_normal)

    lista_normal.sort()
    dll1.ordenar(sortMethod)

    dll1 = fromDllToList(dll1)
    return dll1 == lista_normal


'''
if __name__ == "__main__":
    for lst_norm in [
        [1,2,3,4,5],
        [831,2134,3242,42],
        [],
        [136],

    ]:
        test = {'ins(item)': insTest(lst_norm),
                'len()': lenTest(lst_norm),
                'mostrar()': mostrarTest(lst_norm),
                'existe(item)': existeTest(lst_norm),
                'ver(p)': verTest(lst_norm, ind),
                'rem(item)': remTest(lst_norm, vlr),
                'limpar()': limparTest(lst_norm),
                'vazia()': vaziaTest(lst_norm),
                'order()' : '?'}

        for i in test:
            print(f'{i} --> {test[i]}')
'''

dll = fromListToDll([5,4,3,2,1,1])
cll = fromListToCll([1,3,4,5,6,674,2,2,21])

