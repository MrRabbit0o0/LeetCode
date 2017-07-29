# coding: utf8


class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        total_sum = sum(A)
        l_max = 0
        for i in range(len(A)):
            l_max += i * A[i]
        g_max = l_max
        for i in range(len(A))[::-1]:
            l_max += (total_sum - A[i] * len(A))
            g_max = max(g_max, l_max)
        return g_max

