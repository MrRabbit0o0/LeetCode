# coding: utf8

class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        step = 0
        while n > 1:
            step += 1
            if n % 2 == 0:
                n /= 2
            elif n % 4 == 1 or n == 3:
                n -= 1
            else:
                n += 1
        return step

