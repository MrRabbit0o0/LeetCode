# coding: utf8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return None
        path = [root]
        def pop_min():
            node = path.pop(-1)
            while node:
                path.append(node)
                node = node.left
            min_val = path[-1].val
            node = path.pop(-1)
            if path:
                path[-1].left = None
            if node.right:
                path.append(node.right)
            return min_val
        while k > 0:
            val = pop_min()
            k -= 1
        return val

