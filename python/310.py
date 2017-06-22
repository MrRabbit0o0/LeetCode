# coding: utf8

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = {i:[] for i in range(n)}
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        degree = [len(graph[i]) for i in range(n)]
        remain = n
        while remain > 2:
            del_node = []
            for j in range(n):
                if degree[j] == 1:
                    remain -= 1
                    del_node.append(j)
                    degree[j] = -1
            for n in del_node:
                for node in graph[n]:
                    degree[node] -= 1
        print degree
        return [i for i, d in enumerate(degree) if d >= 0]


if __name__ == '__main__':
    n = 6
    edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
    print Solution().findMinHeightTrees(n, edges)
