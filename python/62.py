# coding: utf8

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(1, m):
            dp[i][0] = 1

        for j in range(1, n):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]

        return dp[m-1][n-1]


if __name__ == '__main__':
    import random
    m = random.randint(0, 10)
    n = random.randint(0, 10)
    print m, n
    print Solution().uniquePaths(m, n)
