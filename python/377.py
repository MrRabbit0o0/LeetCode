# coding: utf8


class Solution(object):
    def __init__(self):
        self.dp = {}

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in self.dp:
            return self.dp[target]
        if target == 0:
            return 1
        if target < 0:
            return 0
        ret = sum([self.combinationSum4(nums, target - val) for val in nums])
        self.dp[target] = ret
        return ret
