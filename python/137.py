# coding: utf8

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        b = 0
        for c in nums:
            tmp = (a&~b&~c)|(~a&b&c)
            b = (~a&~b&c)|(~a&b&~c)
            a = tmp
        return a|b

if __name__ == '__main__':
    nums = [2, 2, 3, 2]
    print Solution().singleNumber(nums)
