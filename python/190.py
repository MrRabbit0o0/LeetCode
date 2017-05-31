# coding: utf8

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        for _ in range(32):
            total += n % 2
            n /= 2
        return total
