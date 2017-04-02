# coding: utf8

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 1:
            return [nums]
        result = []
        for i in range(len(nums)):
            p = [[nums[i]] + x for x in self.permute(nums[:i]+ nums[i+1:])]
            result.extend(p)
        return result


if __name__ == '__main__':
    nums = [2, 3, 1]
    nums.sort()
    print nums
    print Solution().permute(nums)
