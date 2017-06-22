# coding: utf8

class NumArray(object):

    from math import sqrt
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        self.m = int(sqrt(2 * n))
        self.buckets = [[] for _ in range(m)]
        self.cums = [0] * m
        for i, n in enumerate(nums):
            bucket = self.buckets[i / m]
            bucket.append(n)
            self.cums[i / m] += n

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        bucket_idx = i / self.m
        bucket = self.buckets[bucket_idx]
        idx = i % self.m
        self.cums[bucket_idx] = self.cums[bucket_idx] - bucket[idx] + val
        bucket[idx] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        start = i / self.m
        end = j / self.m
        start_idx = i % self.m
        end_idx = j % self.m
        total = sum(self.cums[start:end])
        total -= sum(self.buckets[start][:start_idx])
        total += sum(self.buckets[end][:end_idx+1])
        return total



