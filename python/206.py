# coding: utf8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        last = None
        while head:
            tmp = head.next
            head.next = last
            last = head
            head = tmp
        head = last
        return head
