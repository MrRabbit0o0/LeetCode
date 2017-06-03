# coding: utf8

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = {}
        ordering = []
        for edge in prerequisites:
            from_node, to_node = edge[0], edge[1]
            if from_node not in graph:
                graph[from_node] = []
            graph[from_node].append(to_node)
        def dfs(nid, node_stack, traveled):
            sub_ordering = []
            for parent in graph.get(nid, []):
                if parent in node_stack:
                    return None
                if parent in traveled:
                    continue
                traveled.add(parent)
                sub_ordering = dfs(parent, node_stack + [parent], traveled) + sub_ordering
            return [nid] + sub_ordering

        traveled = set()
        for node_id in range(numCourses):
            if node_id in traveled:
                continue
            try:
                traveled.add(node_id)
                sub_ordering = dfs(node_id, [node_id], traveled)
            except:
                return []
            ordering += sub_ordering[::-1]
        return ordering

    def findOrder2(self, numCourses, prerequisites):
        graph = {i: set() for i in range(numCourses)}
        indeg = {i:0 for i in range(numCourses)}
        for j, i in prerequisites:
            graph[i].add(j)
            indeg[j] += 1
        queue = [i for i in range(numCourses) if not indeg[i]]
        ordering = []
        while queue:
            # popleft is BFS, popright is DFS
            node = queue.pop()
            ordering.append(node)
            for parent in graph[node]:
                indeg[parent] -= 1
                if not indeg[parent]:
                    queue.append(parent)
        return ordering if len(ordering) == numCourses else []



if __name__ == '__main__':
    numCourses = 3
    prerequisites = [[0,1],[0,2],[1,2]]
    print Solution().findOrder2(numCourses, prerequisites)
    numCourses = 2
    prerequisites = [[0, 1], [1, 0]]
    print Solution().findOrder2(numCourses, prerequisites)
