# coding: utf8


class Solution(object):
    def __init__(self):
        self.max3power = 3 ** 19

    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return not (n <= 0 or n > self.max3power) and self.max3power % n == 0

