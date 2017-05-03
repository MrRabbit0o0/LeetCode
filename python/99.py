# coding: utf8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.first_node = None
        self.second_node = None
        self.prev_node = None

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def subP(node):
            if not node:
                return
            subP(node.left)
            if not self.first_node and self.prev_node and self.prev_node.val >= node.val:
                self.first_node = self.prev_node
            if self.first_node and self.prev_node and self.prev_node.val >= node.val:
                self.second_node = self.prev_node
            self.prev_node = node
            subP(node.right)
            return

        subP(root)
        self.first_node.val, self.second_node.val = self.second_node.val, self.first_node.val
