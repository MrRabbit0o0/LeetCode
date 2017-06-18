# coding: utf8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        node_list = [root]
        while any(node_list):
            new_node_list = []
            for n in node_list:
                if n:
                    res.append(str(n.val))
                    new_node_list.append(n.left)
                    new_node_list.append(n.right)
                else:
                    res.append('null')
                    new_node_list.append(None)
                    new_node_list.append(None)
            node_list = new_node_list
        return '_'.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        node_list = data.split('_')
        tree_node = []
        for node_val in node_list:
            if node_val != 'null':
                new_node = TreeNode(int(node_val))
                tree_node.append(new_node)
            else:
                tree_node.append(None)
        for i in range(len(tree_node)/2):
            if tree_node[i]:
                tree_node[i].left = tree_node[2*i]
                tree_node[i].right = tree_node[2*i+1]
        return tree_node[0]


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    codec = Codec()
    codec.deserialize(codec.serialize(root))

