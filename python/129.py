# coding: utf8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        sum_list = []
        def dfs(node, pre_sum):
            if not node.right and not node.left:
                total_sum.append(pre_sum + str(node.val))
            pre_sum += str(node.val)
            if node.left:
                dfs(node.left, pre_sum)
            if node.right:
                dfs(node.right, pre_sum)
        dfs(root, '')
        return sum(map(int, sum_list))


