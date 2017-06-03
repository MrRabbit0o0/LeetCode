# coding: utf8

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.arob(nums[1:]), self.arob(nums[:-1]))

    def arob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        T = [-1] * len(nums)
        def sub_rob(i):
            if i >= len(nums):
                return 0
            if T[i] != -1:
                return T[i]
            else:
                T[i] = max(nums[i] + sub_rob(i+2), sub_rob(i+1))
                return T[i]
        return sub_rob(0)



if __name__ == '__main__':
    nums = [11, 2, 5, 3, 4]
    print nums
    print Solution().rob(nums)
