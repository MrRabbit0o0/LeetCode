# coding: utf8

class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        T = [[0] * (n+1) for _ in range(n+1)]
        def subP(s, e):
            if s >= e:
                return 0
            if T[s][e] != 0:
                return T[s][e]
            res = float('inf')
            for x in range(s, e+1):
                tmp = x + max(subP(s, x-1), subP(x+1, e))
                res = min(res, tmp)
            T[s][e] = res
            return res
        return subP(1, n)


if __name__ == '__main__':
    print Solution().getMoneyAmount(12)

