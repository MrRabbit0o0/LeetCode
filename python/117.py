# coding: utf8

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        node_list = [root]
        while node_list:
            new_node_list = []
            for node in node_list:
                new_node_list.append(node.left)
                new_node_list.append(node.right)
            next_node = None
            for node in node_list[::-1]:
                node.next = next_node
                next_node = node
            node_list = filter(lambda x: x, new_node_list)


