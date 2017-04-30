# coding: utf8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        m = 0
        lnode = head
        while lnode:
            lnode = lnode.next
            m += 1
        mid = m / 2
        lnode = head
        last = None
        while mid > 0:
            last = lnode
            lnode = lnode.next
            mid -= 1
        last.next = None
        right = lnode
        left = head
        sorted_left = self.sortList(left)
        sorted_right = self.sortList(right)
        head = self.merge(sorted_left, sorted_right)
        return head

    def merge(self, h1, h2):
        if not h1:
            return h2
        if not h2:
            return h1
        if h1.val < h2.val:
            head = h1
            h1 = h1.next
        else:
            head = h2
            h2 = h2.next
        last = head
        while h1 and h2:
            if h1.val < h2.val:
                last.next = h1
                h1 = h1.next
            else:
                last.next = h2
                h2 = h2.next
            last = last.next
        if not h1:
            last.next = h2
        elif not h2:
            last.next = h1
        return head


if __name__ == '__main__':
    l = [3, 4, 1, 2]
    lnode = ListNode(0)
    head = lnode
    for x in l:
        node = ListNode(x)
        lnode.next = node
        lnode = lnode.next
    head = head.next

    lnode = Solution().sortList(head)

    result = []
    while lnode:
        result.append(lnode.val)
        lnode = lnode.next
    print result
