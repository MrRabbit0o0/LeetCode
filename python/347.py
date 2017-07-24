# coding: utf8


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        bucket = [[] for _ in range(len(nums)+1)]
        for n, c in counter.iteritems():
            bucket[c].append(n)

        result = []
        while k > 0:
            cur = bucket.pop()
            result += cur
            k -= len(cur)
        return result


