# coding: utf8

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        dp = [0]
        MAX_NUMBER = n + 1
        while len(dp) <= n:
            m = len(dp)
            min_num = MAX_NUMBER
            i = 1
            while i ** 2 <= m:
                min_num = min(min_num, dp[m - i**2] + 1)
                i += 1
            dp.append(min_num)
        return dp[-1]



if __name__ == '__main__':
    for n in [12, 13, 9]:
        print n
        print Solution().numSquares(n)

