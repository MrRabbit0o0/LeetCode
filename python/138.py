# coding: utf8

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        lnode = head
        if not lnode:
            return None
        origin_dict = {}
        new_dict = {}
        new_head = RandomListNode(0)
        n_lnode = new_head
        i = 1
        while lnode:
            n_lnode.label = lnode.label
            origin_dict[lnode] = i
            new_dict[i] = n_lnode
            if lnode.next:
                n_lnode.next = RandomListNode(0)
                n_lnode = n_lnode.next
            lnode = lnode.next
            i += 1
        lnode = head
        n_lnode = new_head
        while lnode:
            random_node = lnode.random
            if not random_node:
                n_lnode.random = None
            else:
                i = origin_dict[random_node]
                n_random = new_dict[i]
                n_lnode.random = n_random
            n_lnode = n_lnode.next
            lnode = lnode.next
        return new_head


if __name__ == '__main__':
    input = [1, 2, 3, 4, 3, 3, '#', '#']
    head = RandomListNode(0)
    lnode = head
    for i in range(4):
        node = RandomListNode(input[i])
        lnode.next = node
        lnode = lnode.next
    lnode.next = None
    head = head.next
    rnode = head.next.next
    head.random = rnode
    head.next.random = rnode
    Solution().copyRandomList(head)

