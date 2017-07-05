# coding:utf8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node:
                return [0, 0]
            left = dfs(node.left)
            right = dfs(node.right)
            result = [0, 0]
            result[0] = left[1] + right[1] + node.val
            result[1] = max(left[0], left[1]) + max(right[0], right[1])
            return result
        return max(dfs(root))


