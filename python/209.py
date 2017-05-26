# coding: utf8


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        sum_list = []
        sum_n = 0
        min_length = len(nums) + 1
        for n in nums:
            sum_n += n
            sum_list.append(n)
            if sum_n >= s:
                while sum_list and sum_n >= s:
                    sub_n = sum_list.pop(0)
                    sum_n -= sub_n
                min_length = min(min_length, len(sum_list)+1)
        return min_length if min_length <= len(nums) else 0


if __name__ == '__main__':
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    print s, nums
    print Solution().minSubArrayLen(s, nums)
    s = 0
    nums = [1, 4, 4]
    print s, nums
    print Solution().minSubArrayLen(s, nums)
