# coding: utf8

class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.deque = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.deque.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        tmp = []
        while len(self.deque) > 1:
            tmp.append(self.deque.pop(0))
        last = self.deque.pop(0)
        self.deque = tmp
        return last

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        tmp = []
        last = None
        while len(self.deque) > 0:
            last = self.deque.pop(0)
            tmp.append(last)
        self.deque = tmp
        return last

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.deque) == 0
