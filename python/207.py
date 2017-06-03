# coding: utf8

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        visit = [0] * numCourses
        graph = {}
        def travel(nid, traveled):
            if visit[nid] == -1:
                return False
            if visit[nid] == 1:
                return True
            visit[nid] = -1
            for parent_id in graph.get(nid, []):
                if not dfs(parent_id):
                    return False
            visit[nid] = 1
            return True

        for edge in prerequisites:
            from_node, to_node = edge[0], edge[1]
            if from_node not in graph:
                graph[from_node] = []
            graph[from_node].append(to_node)
        for node_id in range(numCourses):
            if not travel(node_id, [node_id]):
                return False
        return True

