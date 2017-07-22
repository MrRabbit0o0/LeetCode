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
        heap = []
        for n1 in nums1:
            for n2 in nums2:
                if len(heap) < k:
                    heapq.heappush(heap, (-n1-n2, [n1, n2]))
                else:
                    if heap and -heap[0][0] > n1+n2:
                        heapq.heappop(heap)
                        heapq.heappush(heap, (-n1-n2, [n1, n2]))
                    else:
                        break
        return [heapq.heappop(heap)[1] for _ in range(k) if heap]



if __name__ == '__main__':
    nums1 = [-10,-4,0,0,6,6,6,7,10,22,100]
    nums2 = [3,5,6,7,8,100]
    k = 20
    print Solution().kSmallestPairs(nums1, nums2, k)
