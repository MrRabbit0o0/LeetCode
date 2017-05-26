# coding: utf8

class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        tmp = []
        while len(self.stack) > 1:
            tmp.append(self.stack.pop(-1))
        front = self.stack.pop(-1)
        while tmp:
            self.stack.append(tmp.pop(-1))
        return front

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        tmp = []
        while len(self.stack) > 1:
            tmp.append(self.stack.pop(-1))
        front = self.stack[0]
        while tmp:
            self.stack.append(tmp.pop(-1))
        return front

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack) == 0
