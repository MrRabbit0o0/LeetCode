# coding: utf8

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s) + 1
        n = len(p) + 1
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True
        for i in range(0, m):
            for j in range(1, n):
                if p[j-1] != '*':
                    dp[i][j] = i > 0 and dp[i-1][j-1] and (p[j-1] == '?' or s[i-1] == p[j-1])
                else:
                    dp[i][j] = dp[i][j-1] or (i > 0 and (dp[i-1][j-1] or dp[i-1][j]))
        return dp[m-1][n-1]


if __name__ == '__main__':
    s = 'aaaaabaaaa'
    p = 'a*ba*?'
    print s, p
    print Solution().isMatch(s, p)
    s = "abefcdgiescdfimde"
    p = "ab*cd?i*de"
    print s, p
    print Solution().isMatch(s, p)
