# coding: utf8

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count_s = {}
        count_t = {}
        for i, c in enumerate(s):
            count_s[c] = count_s.get(c, '') + str(i)
        for i, c in enumerate(t):
            count_t[c] = count_t.get(c, '') + str(i)
        return set(count_s.itervalues()) == set(count_t.itervalues())
