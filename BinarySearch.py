from doubly_linked_list import DoublyCircularLinkedList
from circular_linked_list import SinglyCircularLinkedList


# noinspection PyUnreachableCode
def binary_search_with_link(linked_list, value):
    raise NotImplementedError  # TODO: write code for binary search with link
    if isinstance(linked_list, SinglyCircularLinkedList) or isinstance(linked_list, DoublyCircularLinkedList):
        pass
    else:
        raise TypeError("linked_list must be a SinglyCircularLinkedList or DoublyCircularLinkedList")


def binary_search_without_link(linked_list, value):
    # O([Dependent]) + O(n) + O(log(n))
    if isinstance(linked_list, SinglyCircularLinkedList) or isinstance(linked_list, DoublyCircularLinkedList):
        l = []
        # O Dependent of implementation
        linked_list.ordernar()
        # O(n)
        for i in linked_list:
            l.append(i)
    else:  # Is already collection
        l = linked_list
    # O(log(n))
    raise NotImplementedError  # TODO: write code for binary search without link

