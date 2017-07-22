# coding: utf8

import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if k < 0 or not nums1 or not nums2:
            return []

        cand = []
        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(cand, (nums1[i] + nums2[j], i, j))
        push(0, 0)
        ret = []
        while cand and len(ret) < k:
            _, i, j = heapq.heappop(cand)
            ret.append((nums1[i], nums2[j]))
            push(i, j + 1)
            if j == 0:
                push(i+1, 0)
        return ret


if __name__ == '__main__':
    nums1 = [-10,-4,0,0,6,6,6,7,10,22,100]
    nums2 = [3,5,6,7,8,100]
    k = 20
    print Solution().kSmallestPairs(nums1, nums2, k)
