# coding: utf8


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        result = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            else:
                if nums1[i] < nums2[j]:
                    i += 1
                else:
                    j += 1
        return result

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        counter1, counter2 = {}, {}
        for n in nums1:
            counter1[n] = counter1.get(n, 0) + 1
        for n in nums2:
            counter2[n] = counter2.get(n, 0) + 1
        result = []
        for n in counter1:
            if n in counter2:
                result += [n] * min(counter1[n], counter2[n])
        return result


