# coding: utf8

class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        f, d = 1, 1
        for i in range(1, length):
            if nums[i] > nums[i-1]:
                f = d + 1
            if nums[i] < nums[i-1]:
                d = f + 1
        return min(length, max(f, d))


