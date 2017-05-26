# coding: utf8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        last = ListNode(head.val - 1)
        last.next = head
        node = head
        new_head = last
        flag = False
        while node:
            if node.next and node.val == node.next.val:
                node.next = node.next.next
                flag = True
            else:
                if flag:
                    last.next = node.next
                else:
                    last = node
                flag = False
                node = node.next
        return new_head.next

