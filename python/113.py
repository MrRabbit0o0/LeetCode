# coding: utf8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        def dfs(node, sub_sum, pre_list):
            if not node:
                return
            if not node.left and not node.right:
                if node.val == sub_sum:
                    result.append(pre_list + [node.val])
                    return
            dfs(node.left, sub_sum-node.val, pre_list + [node.val])
            dfs(node.right, sub_sum-node.val, pre_list + [node.val])
        dfs(root, sum, [])
        return result

