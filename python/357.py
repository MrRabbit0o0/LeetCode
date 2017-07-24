# coding: utf8

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        def per(n, r):
            return n * per(n-1, r-1) if r != 0 else 1
        return 1 + sum([9 * per(9, i) for i in range(min(10, n))])

