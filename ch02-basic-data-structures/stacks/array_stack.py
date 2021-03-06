from __future__ import annotations

from typing import Any, Tuple


class ArrayStack:
    """ArrayStack implements a LIFO stack with a Python list as its underlying storage

    Using the Python list as underlying storage obscures the resizing operations and cost
    associated with dynamic arrays. However, as shown in chapter 1 the amortized cost of
    expanding and shrinking a dynamic array is O(n). Dynamic array constant factors may
    still be a bit fatter than a linked-list, depending on implementation details of each.
    Linked list implementations are likely to use more memory per element due to the need
    to hold references to the next (and previous in the case of a doubly-linked list) node
    """

    def __init__(self):
        self._arr = []

    def __len__(self):
        return len(self._arr)

    def is_empty(self) -> bool:
        return len(self._arr) == 0

    def push(self, val: Any) -> ArrayStack:
        """Push value onto top of LIFO stack"""
        self._arr.append(val)
        return self

    def pop(self) -> Tuple[ArrayStack, Any]:
        """Pop value off top of LIFO stack and return

        Raise Empty exception if stack is empty
        """
        if self.is_empty():
            raise Empty("stack is empty")
        val = self._arr.pop()
        return self, val

    def top(self) -> Tuple[ArrayStack, Any]:
        """Access (but do not remove) value at top of LIFO stack and return

        Raise Empty exception if stack is empty
        """
        if self.is_empty():
            raise Empty("stack is empty")
        val = self._arr[-1]
        return self, val


class Empty(Exception):
    """Error attempting to access and element from an empty container type"""
