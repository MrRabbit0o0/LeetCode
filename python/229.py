# coding: utf8

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        c1, c2, can1, can2 = 0, 0, 0, 1
        for n in nums:
            if n == can1:
                c1 += 1
            elif n == can2:
                c2 += 1
            elif c1 == 0:
                c1, can1 = 1, n
            elif c2 == 0:
                c2, can2 = 1, n
            else:
                c1, c2 = c1 - 1, c2 - 1
        return [n for n in (can1, can2) if nums.count(n) > len(nums)/3]


if __name__ == '__main__':
    nums = [2, 2, 1, 3]
    print nums
    print Solution().majorityElement(nums)
