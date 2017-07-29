# coding: utf8

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == '':
            return True
        if t == '':
            return False
        for i in range(len(t)):
            if s == '':
                return True
            if t[i] == s[0]:
                s = s[1:]
        return s == ''

    def isSubsequence(self, s, t):
        t = iter(t)
        return all(c in t for c in s)


