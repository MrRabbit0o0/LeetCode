# coding: utf8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head
        lnode = head
        l = 0
        while lnode:
            l += 1
            lnode = lnode.next
        if k % l == 0:
            return head
        idx = l - k % l
        lnode = head
        last_node = None
        while idx > 0:
            last_node = lnode
            lnode = lnode.next
            idx -= 1
        new_head = lnode
        last_node.next = None
        while lnode.next:
            lnode = lnode.next
        lnode.next = head
        return new_head



if __name__ == '__main__':
    import random
    input = range(random.randint(0, 20))
    k = random.randint(0, len(input))
    if not input:
        head = None
    else:
        head = ListNode(input[0])
        lnode = head
        for x in input[1:]:
            lnode.next = ListNode(x)
            lnode = lnode.next
    print input
    print k
    result = Solution().rotateRight(head, k)
    r = []
    while result:
        r.append(result.val)
        result = result.next
    print r
