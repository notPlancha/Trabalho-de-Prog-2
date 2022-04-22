from typing import Literal

from doubly_linked_list import DoublyLinkedList, DoublyLinkedNode
from circular_linked_list import CircularLinkedList
from base_classes import LinkedNode

# Doubly Linked List

# Objects and variables that will be used specifically on this test (can be changed)
lst_norm = [4, 3, 2, 1]  # test normal list
vlr = 3  # value
ind = 2  # index (begins on 0)


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


def fromllToList(ll):
    current_node = ll.head
    ret = []
    for current_node in ll:
        ret.append(current_node.value)
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
def insTest(lista_normal, linkedListType='dll'):
    lista_comp = []

    match linkedListType:
        case 'cll':
            cll1 = CircularLinkedList()

            for element_norm in lista_normal:
                cll1.ins(element_norm)

            current_node = cll1.head
            i = 0
            while i != cll1.len():
                lista_comp.append(current_node.value)
                current_node = current_node.next
                i += 1

            return lista_comp == lista_normal

        case _:
            lista_comp_rev = []
            dll1 = DoublyLinkedList()

            for element_norm in lista_normal:
                dll1.ins(element_norm)

            current_node = dll1.tail
            while current_node is not None:
                lista_comp_rev.append(current_node.value)
                current_node = current_node.prev

            current_node = dll1.head

            while current_node is not None:
                lista_comp.append(current_node.value)
                current_node = current_node.next

            lista_comp_rev.reverse()
            return lista_comp == lista_comp_rev == lista_normal


def lenTest(lista_normal, linkedListType='dll'):
    if linkedListType == 'cll':
        cll1 = fromListToCll(lista_normal)
        return len(lista_normal) == len(cll1) == cll1.len() == cll1.size

    dll1 = fromListToDll(lista_normal)
    return len(lista_normal) == len(dll1) == dll1.len() == dll1.size


def mostrarTest(lista_normal, linkedListType='dll'):
    if linkedListType == 'cll':
        cll1 = fromListToCll(lista_normal)
        lst1 = ""

        for i in range(len(lista_normal)):
            if i == len(lista_normal) - 1:
                lst1 += str(lista_normal[i]) + " -> / " + str(lista_normal[0]) + " -> ... "
                break
            lst1 += str(lista_normal[i]) + " -> "
            i += 1

        return lst1 == cll1.mostrar()

    dll1 = fromListToDll(lista_normal)
    lst1 = ' <-> '.join([str(element_norm) for element_norm in lista_normal])
    return lst1 == dll1.mostrar()


# this function searches for a certain value. It returns 0 if the value is not on the linked list,
# otherwise it will return the position of the first element of the linkedlist that equals the given value
def existeTest(lista_normal, linkedListType='dll'):
    lst_string = ''

    for elemento in lista_normal:
        lst_string += str(elemento)

        if linkedListType == 'cll':
            cll1 = fromListToCll(lista_normal)
            for valor in lst_string:
                if (lst_string.find(valor) + 1 != cll1.existe(int(valor))):
                    return False
            return True

        dll1 = fromListToDll(lista_normal)
        for valor in lst_string:
            if (lst_string.find(valor) + 1 != dll1.existe(int(valor))):
                return False
        return True


def verTest(lista_normal, linkedListType='dll'):
    if linkedListType == 'cll':
        cll1 = fromListToCll(lista_normal)
        for i in range(len(lista_normal)):
            if lista_normal[i] != cll1.ver(i):
                return False
        return True

    dll1 = fromListToDll(lista_normal)
    for i in range(len(lista_normal)):
        if lista_normal[i] != dll1.ver(i):
            return False
    return True


def remTest(lista_normal, item, linkedListType = 'dll'):  # item tem que estar na lista
    if linkedListType == 'cll':
        cll1 = fromListToCll(lista_normal)
        try:
            lista_normal.remove(item)
        except ValueError:
            return cll1.rem(item) is False
        cll1.rem(item)
        cll1 = fromllToList(cll1)
        return cll1 == lista_normal

    dll1 = fromListToDll(lista_normal)
    try:
        lista_normal.remove(item)
    except ValueError:
        return dll1.rem(item) is False
    dll1.rem(item)
    dll1 = fromllToList(dll1)
    return dll1 == lista_normal



def limparTest(lista_normal, linkedListType='dll'):
    if linkedListType == 'cll':
        cll1 = fromListToCll(lista_normal)
        cll1.limpar()
        lista_comp = fromllToList(cll1)
        return lista_comp == []

    dll1 = fromListToDll(lista_normal)
    dll1.limpar()

    lista_comp = fromllToList(dll1)

    return lista_comp == []


def vaziaTest(lista_normal, linkedListType='dll'):
    if linkedListType == 'cll':
        cll1 = fromListToCll(lista_normal)
        lst1 = fromllToList(cll1)
        cll2 = CircularLinkedList()

        return (cll1.vazia() == (len(lst1) == 0)) and (cll2.vazia())

    dll1 = fromListToDll(lista_normal)
    lst1 = fromllToList(dll1)

    dll2 = DoublyLinkedList()
    return (dll1.vazia() == (len(lst1) == 0)) and (dll2.vazia())



def ordenarTest(lista_normal, linkedListType = 'dll'):

    if linkedListType == 'dll':
        cll1 = fromListToCll(lista_normal)
        cll2 = fromListToCll(lista_normal)

        lista_normal.sort()
        cll1.ordenar('b')
        cll2.ordenar('m')

        return fromllToList(cll1) == lista_normal == fromllToList(cll2)

    dll1 = fromListToDll(lista_normal)
    dll2 = fromListToDll(lista_normal)

    lista_normal.sort()
    dll1.ordenar('b')
    dll2.ordenar('m')

    return fromllToList(dll1) == lista_normal == fromllToList(dll2)


def binarySearchTest(lista_normal, item):
    dll1 = fromListToDll(lista_normal)
    pass
'''


if __name__ == "__main__":
    print('Doubly Linked List Tests', end='\n\n')
    '''
    n = 1
    for lst_norm in [
        [1,2,3,4,5],
        [831,2134,3242,42],
        [],
        [136]]:

        print(n, end='\n\n')
    n += 1
    
    '''

    test = {'ins(item)': insTest(lst_norm),
            'len()': lenTest(lst_norm),
            'mostrar()': mostrarTest(lst_norm),
            'existe(item)': existeTest(lst_norm),
            'ver(p)': verTest(lst_norm),
            'rem(item)': remTest(lst_norm, vlr),
            'limpar()': limparTest(lst_norm),
            'vazia()': vaziaTest(lst_norm)}
            #'order()': ordenarTest(lst_norm)}
    # , 'binarySearch(item)': binarySearchTest(lst_norm, vlr)}

    for i in test:
        print(f'{i} --> {test[i]}')

    # Circular Linked List

    '''
    n = 1
    for lst_norm in [
        [1,2,3,4,5],
        [831,2134,3242,42],
        [],
        [136]]:

        print(n, end='\n\n')
    n += 1

    '''
    print('\n\nCircular Linked List Tests', end='\n\n')

    test = {'ins(item)': insTest(lst_norm, 'cll'),
            'len()': lenTest(lst_norm, 'cll'),
            'mostrar()': mostrarTest(lst_norm, 'cll'),
            'existe(item)': existeTest(lst_norm, 'cll'),
            'ver(p)': verTest(lst_norm, 'cll'),
            'rem(item)': remTest(lst_norm, vlr, 'cll'),
            'limpar()': limparTest(lst_norm, 'cll'),
            'vazia()': vaziaTest(lst_norm, 'cll'),
            'order()': ordenarTest(lst_norm, 'cll')}

    for i in test:
        print(f'{i} --> {test[i]}')

    cll = fromListToCll([1, 20, 4, 5])  # Todo erase this in case i forget
    dll = fromListToDll([4, 3, 2, 1])  # Todo erase this in case i forget
