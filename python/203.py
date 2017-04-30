# coding: utf8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        node = ListNode(0)
        node.next = head
        new_head = node
        last = node
        node = node.next
        while node:
            if node.val == val:
                next_node = node.next
                while next_node and next_node.val == val:
                    next_node = next_node.next
                if next_node:
                    last.next = next_node
                    last = next_node
                else:
                    last.next = None
                    break
                node = next_node
            else:
                last = node
                node = node.next
        return new_head.next


if __name__ == '__main__':
    l = [1, 2, 2, 2]
    lnode = ListNode(0)
    head = lnode
    for x in l:
        node = ListNode(x)
        lnode.next = node
        lnode = lnode.next
    head = head.next

    lnode = Solution().removeElements(head, 2)

    result = []
    while lnode:
        result.append(lnode.val)
        lnode = lnode.next
    print result
