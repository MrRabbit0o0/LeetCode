# coding: utf8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        node_list = [root]
        while node_list and node_list[0]:
            depth += 1
            new_node_list = []
            for node in node_list:
                if node.left:
                    new_node_list.append(node.left)
                if node.right:
                    new_node_list.append(node.right)
            node_list = new_node_list
        return depth


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def subP(node_list):
            if not node_list or not node_list[0]:
                return 0
            new_node_list = []
            for node in node_list:
                if node.left:
                    new_node_list.append(node.left)
                if node.right:
                    new_node_list.append(node.right)
            return subP(new_node_list) + 1
        return subP([root])
