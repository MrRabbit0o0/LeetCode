# coding: utf8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        def dfs(pre, node):
            if not node:
                return
            if not node.left and not node.right:
                res.append(pre + [str(node.val)])
                return
            dfs(pre + [str(node.val)], node.left)
            dfs(pre + [str(node.val)], node.right)
        dfs([], root)
        return map('->'.join, res)


