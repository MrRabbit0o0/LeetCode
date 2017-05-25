# coding: utf8

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        max_area = 0
        m = len(matrix)
        n = len(matrix[0])
        def get_height(l):
            height = 0
            while height < len(l) and l[height] == '1':
                height += 1
            return height

        for j in range(n):
            heights = []
            for i in range(m):
                heights.append(get_height(matrix[i][j:]))
            max_area = max(max_area, self.largestRect(heights))
        return max_area

    def largestRect(self, heights):
        ret = 0
        heights.append(0)
        index = []
        for i in range(len(heights)):
            while index and heights[index[-1]] >= heights[i]:
                h = heights[index.pop(-1)]
                sidx = index[-1] if index else -1
                ret = max(ret, h * (i-sidx-1))
            index.append(i)
        return ret


if __name__ == '__main__':
    matrix = ["10100","10111","11111","10010"]
    print Solution().maximalRectangle(matrix)

