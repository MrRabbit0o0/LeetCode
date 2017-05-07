# coding: utf8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder and not inorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(0)
        root.val = preorder[0]
        root_index = inorder.index(root.val)
        split_index = root_index
        root.left = self.buildTree(preorder[1:split_index+1], inorder[:root_index])
        root.right = self.buildTree(preorder[split_index+1:], inorder[root_index+1:])
        return root


if __name__ == '__main__':
    from utils import tree2list
    preorder = [1, 2]
    inorder = [1, 2]
    root = Solution().buildTree(preorder, inorder)
    print tree2list(root)
    preorder = [3, 2, 1 ,4]
    inorder = [1, 2, 3, 4]
    root = Solution().buildTree(preorder, inorder)
    print tree2list(root)
    preorder = [7,-10,-4,3,-1,2,-8,11]
    inorder = [-4,-10,3,-1,7,11,-8,2]
    root = Solution().buildTree(preorder, inorder)
    print tree2list(root)
