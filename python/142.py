# coding: utf8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        runner = head
        walker = head
        cycle_node = None
        while runner.next and runner.next.next:
            if walker.next is runner.next.next:
                cycle_node = walker.next
                break
            walker = walker.next
            runner = runner.next.next
        if not cycle_node:
            return None
        walker = head
        while walker is not cycle_node:
            walker = walker.next
            cycle_node = cycle_node.next
        return walker


if __name__ == '__main__':
    head = ListNode(3)
    n1 = ListNode(2)
    head.next = n1
    n1.next = head
    result = Solution().detectCycle(head)
    print result and result.val
    print '....'

    head = ListNode(3)
    n1 = ListNode(2)
    head.next = n1
    n2 = ListNode(0)
    n1.next = n2
    n3 = ListNode(-4)
    n2.next = n3
    n3.next = n1
    result = Solution().detectCycle(head)
    print result and result.val
