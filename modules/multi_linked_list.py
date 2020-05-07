# classes implementations are partly based on Data Structures and Algorithms Using Python – R. Necaise
# These classes implementations are mostly implemented for usage of a one multi-linked list node,
# just like a demultiplexer, which is completely enough for my adt.


class DoubleMLinkedList:
    """ Class for double linked list representation. """

    def __init__(self, item):
        """ Create new double linked list. """
        self._head = _DoubleMLinkedListNode(item)

    def head(self):
        """ Return head of the double linked list. """
        return self._head

    def add_one_way(self, item):
        """ Add an item the one way of the double linked list. """
        self._head.one_way = item

    def add_second_way(self, item):
        """ Add an item the second way of the double linked list. """
        self._head.second_way = item


class TripleMLinkedList:
    """ Class for triple linked list representation. """

    def __init__(self, item):
        """ Create new triple linked list. """
        self._head = _TripleMLinkedListNode(item)

    def head(self):
        """ Return head of the triple linked list. """
        return self._head

    def add_one_way(self, item):
        """ Add an item the one way of the triple linked list. """
        self._head.one_way = item

    def add_second_way(self, item):
        """ Add an item the second way of the triple linked list. """
        self._head.second_way = item

    def add_third_way(self, item):
        """ Add an item the third way of the triple linked list. """
        self._head.third_way = item


class _DoubleMLinkedListNode:
    """ Class for double linked list node representation. """

    def __init__(self, item):
        """ Create new double linked list node. """
        self.item = item
        self.one_way = None
        self.second_way = None


class _TripleMLinkedListNode:
    """ Class for triple linked list node representation. """

    def __init__(self, item):
        """ Create new triple linked list node. """
        self.item = item
        self.one_way = None
        self.second_way = None
        self.third_way = None
