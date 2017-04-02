# coding: utf8

class Solution(object):
    def canjump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return True
        last = len(nums) - 1
        i = last - 1
        while i >= 0:
            if nums[i] + i >= last:
                last = i
            i -= 1
        return last <= 0



if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    print nums
    print Solution().canjump(nums)
