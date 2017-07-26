# coding: utf8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        self.length = 0
        while head:
            self.length += 1
            head = head.next

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        node = self.head
        idx = random.randint(1, self.length)
        while idx > 1:
            node = node.next
            idx -= 1
        return node.val


