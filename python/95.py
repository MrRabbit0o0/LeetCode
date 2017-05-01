# coding: utf8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        val_list = range(1, n+1)
        def subG(l):
            if not l:
                return [None]
            result = []
            for i in range(len(l)):
                ltree_list = subG(l[:i])
                rtree_list = subG(l[i+1:])
                for lnode in ltree_list:
                    for rnode in rtree_list:
                        root = TreeNode(l[i])
                        root.left = lnode
                        root.right = rnode
                        result.append(root)
            return result
        return subG(val_list)


