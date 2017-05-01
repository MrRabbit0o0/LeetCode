# coding: utf8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        new_head = ListNode(0)
        new_head.next = head
        lnode = head
        idx = new_head
        last = new_head
        while lnode:
            if lnode.val < x:
                if last == idx:
                    last = lnode
                    idx = idx.next
                    lnode = lnode.next
                else:
                    last.next = lnode.next
                    lnode.next = idx.next
                    idx.next = lnode
                    lnode = last.next
                    idx = idx.next
            else:
                last = lnode
                lnode = lnode.next
        return new_head.next


if __name__ == '__main__':
    l = [1, 4, 3, 2, 5, 0]
    x = 3
    lnode = ListNode(0)
    head = lnode
    for n in l:
        node = ListNode(n)
        lnode.next = node
        lnode = lnode.next
    head = head.next
    input_l = []
    lnode = head
    while lnode:
        input_l.append(lnode.val)
        lnode = lnode.next
    print input_l

    lnode = Solution().partition(head, x)

    result = []
    while lnode:
        result.append(lnode.val)
        lnode = lnode.next
    print result
