# coding: utf8

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = range(n)
        for i in range(n):
            for j in range(1, i):
                dp[i] = max(dp[i], max(j, dp[j-1]) * max(i-j+1, dp[i-j]))
        return dp[-1]


if __name__ == '__main__':
    for n in [2, 10]:
        print n
        print Solution().integerBreak(n)
