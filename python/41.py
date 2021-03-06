# coding: utf8

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while  i < len(nums):
            if 0 < nums[i] < len(nums) and nums[i] != i+1:
                if nums[nums[i]-1] == nums[i]:
                    i += 1
                else:
                    nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]- 1]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1


if __name__ == '__main__':
    nums = [3, 4, -1, 1]
    print Solution().firstMissingPositive(nums)
    nums = [3, 3, 3, 4, -1, 1]
    print Solution().firstMissingPositive(nums)
    nums = [1, 1]
    print Solution().firstMissingPositive(nums)
    nums = [2]
    print Solution().firstMissingPositive(nums)
