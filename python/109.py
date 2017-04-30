# coding: utf8

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        n = 0
        lnode = head
        while lnode:
            lnode = lnode.next
            n += 1
        if n == 0:
            return None
        if n == 1:
            return TreeNode(head.val)
        mid = (n+1) / 2 - 1
        print n, mid
        lnode = head
        last = None
        while mid > 0:
            last = lnode
            lnode = lnode.next
            mid -= 1
        mid_node = lnode
        right = mid_node.next
        if last:
            last.next = None
            left = head
        else:
            left = None
        root = TreeNode(mid_node.val)
        root.left = self.sortedListToBST(left)
        root.right = self.sortedListToBST(right)
        return root

