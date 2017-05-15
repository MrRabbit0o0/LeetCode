# coding: utf8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        node_list = [root]
        while any(node_list):
            node = node_list.pop(0)
            if not node:
                continue
            result.append(node.val)
            node_list = [node.left, node.right] + node_list
        return result


