# coding: utf8

class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def oneMax(n1, sk):
            drop_count = len(n1) - sk
            out = []
            for n in n1:
                while drop_count and out and out[-1] < n:
                    out.pop(-1)
                    drop_count -= 1
                out.append(n)
            return out[:sk]

        def merge(a, b):
            return [max(a, b).pop(0) for _ in a + b]

        return max(merge(oneMax(nums1, i), oneMax(nums2, k - i))
                   for i in range(k+1) if i <= len(nums1) and k - i <= len(nums2))



if __name__ == '__main__':
    nums1 = [9, 1, 2, 5, 8, 3]
    nums2 = [3, 4, 6, 5]
    k = 5
    print Solution().maxNumber(nums1, nums2, k)
