# coding: utf8

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        h = 1
        for i in range(len(citations)-1):
            if citations[i] < h:
                return h - 1
            elif citations[i] >= h and citations[i+1] < h:
                return h
            else:
                h += 1
        if citations and citations[-1] >= h:
            return h
        else:
            return h - 1


if __name__ == '__main__':
    citations = [10, 8, 9]
    print citations
    print Solution().hIndex(citations)
    citations = [3, 0, 6, 1, 5]
    print citations
    print Solution().hIndex(citations)
    citations = [0,1]
    print citations
    print Solution().hIndex(citations)
    citations = [1, 1]
    print citations
    print Solution().hIndex(citations)
