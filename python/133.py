# coding: utf8

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        cloned_node = {}
        def clone(gnode):
            if gnode.label in cloned_node:
                return cloned_node[gnode.label]
            new_node = UndirectedGraphNode(gnode.label)
            for tocloned_node in gnode.neighbors:
                if tocloned_node.label == gnode.label:
                    new_node.neighbors.append(new_node)
                else:
                    new_node.neighbors.append(clone(tocloned_node))
            cloned_node[gnode.label] = new_node
            return new_node
        return clone(node)

