# coding: utf8

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ret = 0
        heights.append(0)
        index = []
        for i in range(len(heights)):
            while index and heights[index[-1]] >= heights[i]:
                h = heights[index[-1]]
                index.pop(-1)
                sidx = index[-1] if index else -1
                ret = max(ret, h * (i-sidx-1))
            index.append(i)
        return ret


if __name__ == '__main__':
    heights = [2, 1, 5, 6, 2, 3]
    print Solution().largestRectangleArea(heights)


