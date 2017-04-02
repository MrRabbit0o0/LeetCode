# coding: utf8

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not all(obstacleGrid):
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0
        dp[0][0] = 1

        for i in range(1, m):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = dp[i-1][0]
            else:
                dp[i][0] = 0

        for j in range(1, n):
            if obstacleGrid[0][j] != 1:
                dp[0][j] = dp[0][j-1]
            else:
                dp[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = 0
        return dp[m-1][n-1]


if __name__ == '__main__':
    import random
    m = random.randint(0, 10)
    n = random.randint(0, 10)
    obstacleGrid = [[0] * n for _ in range(m)]
    obstacle_num = random.randint(0, m * n / 2)
    for _ in range(obstacle_num):
        i = random.randint(0, m-1)
        j = random.randint(0, n-1)
        obstacleGrid[i][j] = 1
    print obstacleGrid
    for x in obstacleGrid:
        print x
    print Solution().uniquePathsWithObstacles(obstacleGrid)
