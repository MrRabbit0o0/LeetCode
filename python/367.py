# coding: utf8

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        base = 1
        while num > 0:
            num -= base
            base += 2
        return num == 0


