# coding: utf8

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = (len(nums) - k) % len(nums)
        for _ in range(n):
            nums.append(nums.pop(0))

    def rotate(self, nums, k):
        import fractions
        length = len(nums)
        k = (length - k) % length
        for i in range(fractions.gcd(length, k)):
            first = i
            tmp = nums[i]
            idx = first
            while (idx + k) % length != first:
                next_idx = (idx + k) % length
                nums[idx] = nums[next_idx]
                idx = next_idx
            nums[idx] = tmp


