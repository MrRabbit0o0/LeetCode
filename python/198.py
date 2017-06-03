# coding: utf8

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        T = [-1] * len(nums)
        T[-1] = nums[-1]
        def subP(i):
            if i >= len(nums):
                return 0
            if T[i] != -1:
                return T[i]
            T[i] = max(nums[i] + subP(i+2), subP(i+1))
            return T[i]
        subP(0)
        return T[0]


if __name__ == '__main__':
    nums = [1, 2]
    print nums
    print Solution().rob(nums)
