# coding: utf8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder and not inorder:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        root = TreeNode(0)
        root.val = postorder[-1]
        root_index = inorder.index(root.val)
        split_index = root_index
        root.left = self.buildTree(inorder[:root_index], postorder[:split_index])
        root.right = self.buildTree(inorder[root_index+1:], postorder[split_index:-1])
        return root


if __name__ == '__main__':
    from utils import tree2list
    inorder = [2, 3, 4, 9, 14, 20, 15]
    postorder = [2, 4, 3, 14, 15, 20, 9]
    root = Solution().buildTree(inorder, postorder)
    print tree2list(root)
    inorder = [1, 2, 3, 4]
    postorder = [4, 3, 2, 1]
    root = Solution().buildTree(inorder, postorder)
    print tree2list(root)
