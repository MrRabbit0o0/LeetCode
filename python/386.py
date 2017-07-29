# coding: utf8


class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # DFS
        res = []
        def dfs(seed):
            if seed > n:
                return
            res.append(seed)
            for a in range(10):
                if seed * 10 > n:
                    return
                dfs(seed * 10 + a)
            return
        for i in range(1, 10):
            dfs(i)
        return res

    def lexicalOrder(self, n):
        res = [1]
        while len(res) < n:
            new = res[-1] * 10
            while new > n:
                new /= 10
                new += 1
                while new % 10 == 0:
                    new /= 10
            res.append(new)
        return res



