# coding: utf8

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        window = []
        res = []
        for i in range(len(nums)):
            if window and window[0] == i-k:
                window.pop(0)
            while window and nums[window[-1]] < nums[i]:
                window.pop(-1)
            window.append(i)
            if i >= k-1:
                res.append(nums[window[0]])
        return res


if __name__ == '__main__':
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print k, nums
    print Solution().maxSlidingWindow(nums, k)
