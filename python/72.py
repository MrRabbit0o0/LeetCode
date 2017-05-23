# coding: utf8

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        dp = [[1] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(min(dp[i][j+1], dp[i+1][j]), dp[i][j]) + 1
        return dp[m][n]


if __name__ == '__main__':
    word1 = 'woid'
    word2 = 'word'
    print word1, word2
    print Solution().minDistance(word1, word2)

    word1 = "plasma"
    word2 = "altruism"
    print word1, word2
    print Solution().minDistance(word1, word2)

    word1 = "dinitrophenylhydrazine"
    word2 = "acetylphenylhydrazine"
    print word1, word2
    print Solution().minDistance(word1, word2)
