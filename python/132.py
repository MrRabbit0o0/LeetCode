# coding: utf8

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return 0
        T = [[0] * len(s) for _ in range(len(s))]
        cut = [0] * len(s)
        for i in range(len(s)):
            min_cut = i
            for j in range(i+1):
                if s[j] == s[i] and (i - j <=2  or T[j+1][i-1]):
                    T[j][i] = True
                    min_cut = 0 if j == 0 else min(min_cut, cut[j-1] + 1)
            cut[i] = min_cut
        return cut[-1]


if __name__ == '__main__':
    s = 'aa'
    print s
    print Solution().minCut(s)
    s = 'aab'
    print s
    print Solution().minCut(s)
