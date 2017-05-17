# coding: utf8

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best = 0
        T = {}
        for n in nums:
            if n in T:
                continue
            T[n] = T.get(n-1, 0) + T.get(n+1, 0) + 1
            T[n + T.get(n+1, 0)] = T[n - T.get(n-1, 0)] = T[n]
            best = max(best, T[n])
        return best

if __name__ == '__main__':
    nums = [100, 1, 40, 2, 4, 3]
    print Solution().longestConsecutive(nums)
