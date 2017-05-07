# coding: utf8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        def subP(node_list, flag):
            if not node_list:
                return
            new_node_list = []
            level_val = []
            for node in node_list:
                level_val.append(node.val)
                if node.left:
                    new_node_list.append(node.left)
                if node.right:
                    new_node_list.append(node.right)
            result.append(level_val[::flag])
            subP(new_node_list, flag * -1)
        if root:
            subP([root], 1)
        return result

