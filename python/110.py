# coding: utf8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if not self.isBalanced(root.left) or not self.isBalanced(root.right):
            return False
        return abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1

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

