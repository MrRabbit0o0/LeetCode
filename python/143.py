# coding: utf8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        lnode = head
        if not lnode or not lnode.next:
            return
        m = 0
        while lnode:
            m += 1
            lnode = lnode.next
        half_i = (m+1) / 2 + 1
        print m, half_i
        lnode = head
        while half_i > 1:
            lnode = lnode.next
            half_i -= 1
        hnode = lnode
        # reverse
        last = None
        while hnode:
            tmp = hnode.next
            hnode.next = last
            last = hnode
            hnode = tmp
        hnode = last
        lnode = head
        while hnode:
            tmp = lnode.next
            lnode.next = hnode
            hnode = hnode.next
            lnode = lnode.next
            lnode.next = tmp
            lnode = lnode.next
        if lnode:
            lnode.next = None


if __name__ == '__main__':
    l = [1, 2, 3, 4]
    lnode = ListNode(0)
    head = lnode
    for x in l:
        node = ListNode(x)
        lnode.next = node
        lnode = lnode.next
    head = head.next

    Solution().reorderList(head)

    result = []
    lnode = head
    while lnode:
        result.append(lnode.val)
        lnode = lnode.next
    print result
