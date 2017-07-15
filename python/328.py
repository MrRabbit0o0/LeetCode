# coding: utf8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        length = 0
        node = head
        tail = None
        while node:
            length += 1
            tail = node
            node = node.next
        if length <= 2:
            return head
        node = head
        step = length / 2
        while step > 0:
            tmp = node.next
            node.next = node.next.next
            node = node.next
            tail.next = tmp
            tmp.next = None
            tail = tail.next
            step -= 1
        return head


