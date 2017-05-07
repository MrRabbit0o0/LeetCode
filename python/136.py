# coding: utf8

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for x in nums:
            count[x] = count.get(x, 0) + 1
        for k, v in count.iteritems():
            if v == 1:
                return k

