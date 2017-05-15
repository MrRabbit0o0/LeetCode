# coding: utf8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        node = root
        ld = 0
        while node:
            ld += 1
            node = node.left
        node = root
        rd = 0
        while node:
            rd += 1
            node = node.right
        total_count = 2 ** ld - 1
        if ld == rd:
            return total_count
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)


