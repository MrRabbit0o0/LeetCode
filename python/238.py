# coding: utf8

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = []
        p = 1
        for n in nums:
            count.append(p)
            p *= n
        p = 1
        for i in range(len(nums)-1, -1, -1):
            count[i] = count[i] * p
            p *= nums[i]
        return count

