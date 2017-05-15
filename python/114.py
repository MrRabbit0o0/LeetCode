# coding: utf8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        tmp = root.right
        tail = root
        if root.left:
            self.flatten(root.left)
            root.right = root.left
            node = root
            while node.right:
                node = node.right
            tail = node
        if tmp:
            self.flatten(tmp)
        tail.right = tmp
        root.left = None

