# coding: utf8

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        return self.permuteSubP(nums)

    def permuteSubP(self, nums):
        if len(set(nums)) <= 1:
            return [nums]
        result = []
        last = None
        for i in range(len(nums)):
            if last == nums[i]:
                continue
            p = [[nums[i]] + x for x in self.permuteUnique(nums[:i]+ nums[i+1:])]
            result.extend(p)
            last = nums[i]
        return result


if __name__ == '__main__':
    nums = [2, 1, 1]
    nums.sort()
    print nums
    print Solution().permuteUnique(nums)
