# coding: utf8

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_element = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.min_element or self.min_element[-1] > x:
            self.min_element.append(x)
        else:
            self.min_element.append(self.min_element[-1])

    def pop(self):
        """
        :rtype: void
        """
        self.min_element.pop(-1)
        return self.stack.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_element[-1]

