# coding: utf8

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return sum(map(lambda x: int(x), str(sum(map(lambda x: int(x), str(sum(map(lambda x: int(x), str(num)))))))))

    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return 1 + (n-1) % 9
