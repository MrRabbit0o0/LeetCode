# coding: utf8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def subP(node):
            #rtype: root-leaf sum, inner sum
            if not node.left and not node.right:
                return node.val, node.val
            l_leaf = r_leaf = 0
            l_inner = r_inner = None
            if node.left:
                l_leaf, l_inner = subP(node.left)
            if node.right:
                r_leaf, r_inner = subP(node.right)
            n_leaf = max(max(l_leaf, r_leaf), 0) + node.val
            n_inner = max(max(l_inner, r_inner), max(0, l_leaf) + max(0, r_leaf) + node.val)
            return n_leaf, n_inner
        _, root_inner = subP(root)
        return root_inner

