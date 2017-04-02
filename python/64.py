# coding: utf8

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not all(grid):
            return 0
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]

        return dp[m-1][n-1]


if __name__ == '__main__':
    import random
    m = random.randint(0, 10)
    n = random.randint(0, 10)
    grid = [[random.randint(0, 100) for _ in range(n)] for x in range(m)]
    print grid
    for x in grid:
        print x
    print Solution().minPathSum(grid)
