# coding: utf8

import collections

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return ''.join(list(collections.Counter(t)-collections.Counter(s)))
