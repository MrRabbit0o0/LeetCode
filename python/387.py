# coding: utf8

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = {}
        for i, c in enumerate(s):
            if c not in index:
                index[c] = i
            else:
                index[c] = None
        min_index = len(s) + 1
        for idx in index.itervalues():
            if idx is not None:
                min_index = min(min_index, idx)
        return -1 if min_index == len(s) + 1 else min_index


