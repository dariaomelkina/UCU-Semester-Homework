# class implementation is mostly based on Data Structures and Algorithms Using Python – R. Necaise
import ctypes


class List:
    """ Class for list/array representation."""

    def __init__(self, size):
        """
        (List, int) -> NoneType
        Create new list.
        """
        self._size = size
        py_array_type = ctypes.py_object * size
        self._elements = py_array_type()
        self.clear(None)

    def __len__(self):
        """
        (List) -> int
        Return size of the list.
        """
        return self._size

    def __getitem__(self, index):
        """
        (List, int) -> object
        Return element by index
        """
        return self._elements[index]

    def __setitem__(self, index, value):
        """
        (List, int, object) -> NoneType
        Set a new value by index.
        """
        self._elements[index] = value

    def clear(self, value):
        """
        (List, object) -> NoneType
        Set all the entries to the value.
        """
        for i in range(len(self)):
            self._elements[i] = value

    def __iter__(self):
        """
        (List) -> _ListIterator
        Iterate through list.
        """
        return _ListIterator(self._elements)

    def add(self, item):
        """
        (List, object) -> NoneType
        Add an item to a first free place in the list,
        if there is one.
        """
        for i in range(self._size):
            if self[i] is None:
                self[i] = item
                break

    def __str__(self):
        """
        (List) -> str
        Return string representation of the list.
        """
        st = '['
        for i in range(self._size):
            st += str(self[i]) + ', '
        return st[:-2] + ']'


class _ListIterator:
    def __init__(self, the_array):
        """
        (_ListIterator, List) -> NoneType
        Create new list iterator.
        """
        self._array_ref = the_array
        self._cur_index = 0

    def __iter__(self):
        """
        (_ListIterator) -> _ListIterator
        Iterate through the list iterator.
        """
        return self

    def __next__(self):
        """
        (_ListIterator) -> object/exception
        Return the next entry.
        """
        if self._cur_index < len(self._array_ref):
            entry = self._array_ref[self._cur_index]
            self._cur_index += 1
            return entry
        else:
            raise StopIteration
