# coding: utf8

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        j = 0
        m = len(s)
        for i in range(m-1, -1, -1):
            if s[j] == s[i]:
                j += 1
        if j == m:
            return s
        return s[j:][::-1] + self.shortestPalindrome(s[:j]) + s[j:]


if __name__ == '__main__':
    s = 'aacecaaa'
    print s
    print Solution().shortestPalindrome(s)
    s = 'ab'
    print s
    print Solution().shortestPalindrome(s)

