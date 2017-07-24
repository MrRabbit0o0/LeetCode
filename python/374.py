# coding: utf8

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lf, rt = 1, n
        while lf < rt:
            mid = (lf + rt) / 2
            if guess(mid) == 1:
                lf = mid + 1
            else:
                rt = mid
        return lf

