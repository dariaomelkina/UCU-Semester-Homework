# class implementation is based on Data Structures and Algorithms Using Python – R. Necaise


class LinkedList:
    """ Class for linked list representation. """

    def __init__(self, item):
        """ Create new linked list. """
        self._head = LinkedListNode(item)
        self._size = 1

    def __len__(self):
        """ Return the size of the linked list. """
        return self._size

    def head(self):
        """ Return the head of the linked list. """
        return self._head

    def add(self, item):
        """ Add an item to the linked list. """
        new_node = LinkedListNode(item)
        new_node.next = self._head
        self._head = new_node
        self._size += 1

    def __iter__(self):
        """ Iterate through the linked list. """
        return _LinkedListIterator(self._head)

    def __str__(self):
        """ Return string representation of the linked list. """
        st = ''
        node = self._head
        while node is not None:
            st += str(node.item) + ' - '
            node = node.next
        return st[:-3]


class LinkedListNode:
    """ Class for linked list node representation. """

    def __init__(self, item):
        """ Create new linked list node."""
        self.item = item
        self.next = None

    def __str__(self):
        """ Return the string representation of the linked list node. """
        return "({})".format(self.item)


class _LinkedListIterator:
    """ Class for linked list iterator representation. """

    def __init__(self, list_head):
        """ Create new linked list iterator. """
        self._curNode = list_head

    def __iter__(self):
        """ Iterate through the linked list iterator. """
        return self

    def next(self):
        """ Return the next item. """
        if self._curNode is None:
            raise StopIteration
        else:
            item = self._curNode.item
            self._curNode = self._curNode.next
            return item
