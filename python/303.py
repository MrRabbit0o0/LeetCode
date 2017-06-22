# coding: utf8

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.cum = [0]
        for n in nums:
            self.cum.append(self.cum[-1] + n)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.cum[j+1] - self.cum[i]


