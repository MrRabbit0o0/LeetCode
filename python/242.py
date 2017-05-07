# coding: utf8

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        slist = [0] * 26
        tlist = [0] * 26
        base = ord('a')
        for c in s:
            slist[ord(c) - base] += 1
        for c in t:
            tlist[ord(c) - base] += 1
        return slist == tlist
