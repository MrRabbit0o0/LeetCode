# coding: utf8

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return None
        T = [1] * n
        t2, t3, t5 = 0, 0, 0
        for i in range(1, n):
            T[i] = min(T[t2]*2, T[t3]*3, T[t5]*5)
            if T[i] == T[t2] * 2:
                t2 += 1
            if T[i] == T[t3] * 3:
                t3 += 1
            if T[i] == T[t5] * 5:
                t5 += 1
        return T[n-1]

