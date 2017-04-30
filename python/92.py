# coding: utf8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        n = n - m
        m -= 1
        new_head = ListNode(0)
        new_head.next = head
        lnode = new_head
        while m > 0:
            lnode = lnode.next
            m -= 1
        last_tail = lnode
        lnode = lnode.next
        new_tail = lnode
        next_node = lnode.next
        while n > 0:
            tmp = next_node.next
            next_node.next = lnode
            lnode = next_node
            next_node = tmp
            n -= 1
        last_tail.next = lnode
        new_tail.next = next_node
        return new_head.next

if __name__ == '__main__':
    l = [1, 2, 3, 4, 5]
    m = 2
    n = 4
    lnode = ListNode(0)
    head = lnode
    for x in l:
        node = ListNode(x)
        lnode.next = node
        lnode = lnode.next
    head = head.next

    lnode = Solution().reverseBetween(head, m, n)

    result = []
    while lnode:
        result.append(lnode.val)
        lnode = lnode.next
    print result
