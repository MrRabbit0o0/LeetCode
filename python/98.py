# coding: utf8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        min_n = None
        max_n = None
        def subP(root, min_n, max_n):
            if not root:
                return True
            if root.left and (root.left.val >= root.val or (min_n and root.left.val <= min_n)):
                return False
            if root.right and (root.right.val <= root.val or (max_n and root.right.val >= max_n)):
                return False
            return subP(root.left, min_n, root.val) and subP(root.right, root.val, max_n)
        return subP(root, min_n, max_n)
