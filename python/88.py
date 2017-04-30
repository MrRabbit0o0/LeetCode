# coding: utf8

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0
        while i < n:
            if j == m:
                nums1[j] = nums2[i]
                i += 1
                m += 1
            elif nums2[i] <= nums1[j]:
                for idx in range(m, j, -1):
                    nums1[idx] = nums1[idx-1]
                nums1[j] = nums2[i]
                i += 1
                m += 1
            j += 1


if __name__ == '__main__':
    import random
    nums1 = [0]
    m = random.randint(0, 100)
    n = random.randint(0, 100)
    nums1 = [random.randint(-1000, 1000) for _ in range(m)]
    nums2 = [random.randint(-1000, 1000) for _ in range(n)]
    nums1.sort()
    nums2.sort()
    nums1 = nums1 + [0] * 200
    print nums1[:m]
    print nums2[:n]
    Solution().merge(nums1, m, nums2, n)
    print nums1[:m+n]

