# coding: utf8

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        T = [-1] * (n + 1)
        T[0] = T[1] = 1
        def subN(l):
            if T[l] != -1:
                return T[l]
            if l <= 1:
                return 1
            result = 0
            for i in range(1, l+1):
                ltree_n = subN(i-1)
                rtree_n = subN(l-i)
                result += ltree_n * rtree_n
            T[l] = result
            return result
        return subN(n)

if __name__ == '__main__':
    n = 19
    print Solution().numTrees(n)
