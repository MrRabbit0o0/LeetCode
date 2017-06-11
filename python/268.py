# coding: utf8

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x, y: x ^ y, range(len(nums)+1) + nums)

if __name__ == '__main__':
    nums = [3, 2, 0]
    print Solution().missingNumber(nums)
