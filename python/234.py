# coding: utf8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second = self.reverse(slow.next)
        first = head
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True

    def reverse(self, node):
        last = None
        while node:
            next_node = node.next
            node.next = last
            last = node
            node = next_node
        return last

