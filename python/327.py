# coding: utf8

class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        T = [0]
        for n in nums:
            T.append(T[-1] + n)
        def sort(lo, hi):
            mid = (lo + hi) / 2
            if mid == lo:
                return 0
            count = sort(lo, mid) + sort(mid, hi)
            i = j = mid
            for left in T[lo:mid]:
                while i < hi and T[i] - left < lower:
                    i += 1
                while j < hi and T[j] - left <= upper:
                    j += 1
                count += j - i
            T[lo:hi] = sorted(T[lo:hi])
            return count
        return sort(0, len(T))

