# coding: utf8

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = {}
        for edge, w in zip(equations, values):
            a, b = edge
            if a not in graph:
                graph[a] = {}
            graph[a][b] = w
        for edge, w in zip(equations, values):
            b, a = edge
            if a not in graph:
                graph[a] = {}
            graph[a][b] = 1 / w
        table = {}
        for k, v in graph.iteritems():
            traveled = set([k])
            new_v = {k:1.0}

            new_v.update(v)
            traveled.add(v.iterkeys())

            to_travel = [(a, b) for a, b in v.iteritems()]
            while to_travel:
                for n, weight in to_travel:
                    new_to = []
                    for new_n, new_w in graph.get(n, {}).iteritems():
                        if new_n not in traveled:
                            traveled.add(new_n)
                            new_to.append((new_n, weight * new_w))
                    new_v.update(dict(new_to))
                to_travel = new_to
            for k2, w in new_v.iteritems():
                table[(k, k2)] = w
        return [table.get((q[0], q[1]), -1.0) for q in queries]



if __name__ == '__main__':
    equations = [["a","b"],["b","c"],["bc","cd"]]
    values = [1.5,2.5,5.0]
    queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
    equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
    values = [3.0,4.0,5.0,6.0]
    queries = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]
    print equations
    print values
    print queries
    print Solution().calcEquation(equations, values, queries)

