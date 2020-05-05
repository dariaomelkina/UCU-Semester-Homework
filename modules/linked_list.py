# class implementation is based on Data Structures and Algorithms Using Python – R. Necaise


class LinkedList:
    def __init__(self, item):
        self._head = LinkedListNode(item)
        self._size = 1

    def __len__(self):
        return self._size

    def head(self):
        return self._head

    def add(self, item):
        new_node = LinkedListNode(item)
        new_node.next = self._head
        self._head = new_node
        self._size += 1

    def __iter__(self):
        return _LinkedListIterator(self._head)

    def __str__(self):
        st = ''
        node = self._head
        while node is not None:
            st += str(node.item) + ' - '
            node = node.next
        return st[:-3]


class LinkedListNode:
    def __init__(self, item):
        self.item = item
        self.next = None

    def __str__(self):
        return "({})".format(self.item)


class _LinkedListIterator:
    def __init__(self, list_head):
        self._curNode = list_head

    def __iter__(self):
        return self

    def next(self):
        if self._curNode is None:
            raise StopIteration
        else:
            item = self._curNode.item
            self._curNode = self._curNode.next
            return item
