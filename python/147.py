# coding: utf8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        new_head = ListNode(head.val)
        tail = new_head
        head = head.next
        while head:
            if head.val >= tail.val:
                tail.next = ListNode(head.val)
                tail = tail.next
                head = head.next
                continue
            lnode = new_head
            last = None
            while lnode.val < head.val:
                last = lnode
                lnode = lnode.next
            node = ListNode(head.val)
            node.next = lnode
            if last:
                last.next = node
            else:
                new_head = node
            head = head.next
        return new_head


if __name__ == '__main__':
    l = [3, 2, 4]
    lnode = ListNode(0)
    head = lnode
    for x in l:
        node = ListNode(x)
        lnode.next = node
        lnode = lnode.next
    head = head.next

    lnode = Solution().insertionSortList(head)

    result = []
    while lnode:
        result.append(lnode.val)
        lnode = lnode.next
    print result
