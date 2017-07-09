# coding: utf8

class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        miss = 1
        need = 0
        i = 0
        while miss <=n:
            if i < len(nums) and nums[i] < miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                need += 1
        return need

