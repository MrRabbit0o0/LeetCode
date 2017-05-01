# coding: utf8

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1+s2) != len(s3):
            return False
        m = len(s1) + 1
        n = len(s2) + 1
        T = [[False] * n for _ in range(m)]
        def dfs(i, j):
            if T[i][j]:
                return False
            if i + j == m+n-2:
                return True
            valid = (i < m-1 and s1[i] == s3[i+j] and dfs(i+1, j)) or (j < n-1 and s2[j] == s3[i+j] and dfs(i, j+1))
            if not valid:
                T[i][j] = True
            return valid
        result = dfs(0, 0)
        return result


if __name__ == '__main__':
    s1 = 'a'
    s2 = ''
    s3 = 'a'
    print s1
    print s2
    print s3
    print Solution().isInterleave(s1, s2, s3)
    s1 = 'aabcc'
    s2 = 'dbbca'
    s3 = 'aadbbcbcac'
    print s1
    print s2
    print s3
    print Solution().isInterleave(s1, s2, s3)
    s3 = 'aadbbbaccc'
    print s1
    print s2
    print s3
    print Solution().isInterleave(s1, s2, s3)
