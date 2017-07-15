# coding: utf8

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        dp = [[None] * len(matrix[0]) for _ in matrix]

        def dfs(i, j):
            if dp[i][j]:
                return dp[i][j]
            if matrix[i][j] == '#' or i < 0 or i > len(matrix) - 1 or j < 0 or j > len(matrix[0]) - 1:
                return 1
            cur = matrix[i][j]
            matrix[i][j] = '#'
            max_length = 1
            if i > 0 and matrix[i-1][j] != '#' and matrix[i-1][j] < cur:
                max_length = max(max_length, 1+dfs(i-1, j))
            if i < len(matrix) - 1 and matrix[i+1][j] != '#' and matrix[i+1][j] < cur:
                max_length = max(max_length, 1+dfs(i+1, j))
            if j > 0 and matrix[i][j-1] != '#' and matrix[i][j-1] < cur:
                max_length = max(max_length, 1+dfs(i, j-1))
            if j < len(matrix[0]) - 1 and matrix[i][j+1] != '#' and matrix[i][j+1] < cur:
                max_length = max(max_length, 1+dfs(i, j+1))
            matrix[i][j] = cur
            dp[i][j] = max_length
            return max_length

        max_length = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                max_length = max(max_length, dfs(i, j))
        return max_length


if __name__ == '__main__':
    matrix = [[9,9,4],[6,6,8],[2,1,1]]
    for p in matrix:
        print p
    print Solution().longestIncreasingPath(matrix)

