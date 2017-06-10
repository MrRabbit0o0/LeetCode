# coding: utf8

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num > 0:
            for i in range(2, 6):
                while num % i == 0:
                    num /= i
        return num == 1

