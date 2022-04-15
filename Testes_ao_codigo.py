from doubly_linked_list import DoublyLinkedList, DoublyLinkedNode

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

def fromDlltoList(dll):
    current_node = dll.head
    ret = []
    while current_node is not None:
        ret.append(current_node.value)
        current_node = current_node.next
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
def existeTest(lista_normal, valor):
    dll1 = fromListToDll(lista_normal)
    lst_string = ''

    for elemento in lista_normal:
        lst_string += str(elemento)

    return lst_string.find(str(valor)) + 1 == dll1.existe(valor)

def verTest(lista_normal, indice):
    dll1 = fromListToDll(lista_normal)

    try:
        value = lista_normal[indice]
    except IndexError:
        try:
            dll1.ver(indice)
            return False
        except IndexError:
            return True
        except:
            return False
    try:
        return value == dll1.ver(indice)
    except:
        return False

def remTest(lista_normal, item):
    dll1 = fromListToDll(lista_normal)

    lista_normal_inc = lista_normal.remove(item)
    dll1 = dll1.rem(item)
    dll1 = fromDlltoList(dll1)

    return dll1 == lista_normal_inc

def limparTest(lista_normal):
    dll1 = fromListToDll(lista_normal)

    dll1.limpar()

    lista_comp = fromDlltoList(dll1)

    return lista_comp == []

def vaziaTest():
    dll = DoublyLinkedList()
    return dll.vazia()

#test = {'ins(item)': insTest(lista_norm), 'len()': lenTest(), 'mostrar()': mostrarTest()}#,
        #'existe(item)': existeTest(valor), 'ver(p)': verTest(indice), 'ordenar()': '?', 'rem(item)': '?'
    #, 'limpar()': limpartest(), 'vazia()': vaziatest()}

#for i in test:
    #print(f'{i} --> {test[i]}')



