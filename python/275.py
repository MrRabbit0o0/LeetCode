# coding: utf8

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        length = len(citations)
        l = 0
        r = length - 1
        while l <= r:
            mid = (l + r) / 2
            h = length - mid
            if h > citations[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return length - l


if __name__ == '__main__':
    citations = [0, 0, 4, 4]
    print citations
    print Solution().hIndex(citations)
