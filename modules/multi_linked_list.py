# classes implementations are partly based on Data Structures and Algorithms Using Python – R. Necaise
# These classes implementations are mostly implemented for usage of a one multi-linked list node,
# just like a demultiplexer, which is completely enough for my adt.


class DoubleMLinkedList:
    def __init__(self, item):
        self._head = _DoubleMLinkedListNode(item)

    def head(self):
        return self._head

    def add_one_way(self, item):
        self._head.one_way = item

    def add_second_way(self, item):
        self._head.second_way = item


class TripleMLinkedList:
    def __init__(self, item):
        self._head = _TripleMLinkedListNode(item)

    def head(self):
        return self._head

    def add_one_way(self, item):
        self._head.one_way = item

    def add_second_way(self, item):
        self._head.second_way = item

    def add_third_way(self, item):
        self._head.third_way = item


class _DoubleMLinkedListNode:
    def __init__(self, item):
        self.item = item
        self.one_way = None
        self.second_way = None


class _TripleMLinkedListNode:
    def __init__(self, item):
        self.item = item
        self.one_way = None
        self.second_way = None
        self.third_way = None
