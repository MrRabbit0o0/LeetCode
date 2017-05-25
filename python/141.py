# coding: utf8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        node = head
        while node.next and node.next.next:
            if head.next is node.next.next:
                return True
            head = head.next
            node = node.next.next
        return False
