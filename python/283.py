# coding: utf8

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i = -1
        j = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    print nums
    Solution().moveZeroes(nums)
    print nums
