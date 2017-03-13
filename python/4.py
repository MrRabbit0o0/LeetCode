class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            base = nums1
            seeker = nums2
        else:
            base = nums2
            seeker = nums1

        left = 0
        right = len(seeker)

