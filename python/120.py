# coding: utf8

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) < 1:
            return 0
        last = triangle.pop(-1)
        while triangle:
            for i in range(len(triangle[-1])):
                triangle[-1][i] += min(last[i], last[i+1])
            last = triangle.pop(-1)
        return last[0]

