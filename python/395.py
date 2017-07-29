# coding: utf8

import collections

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if s == '' or k > len(s):
            return 0
        counter = collections.defaultdict(list)
        for i, c in enumerate(s):
            counter[c].append(i)
        split = []
        for v in counter.itervalues():
            if len(v) < k:
                split += v
        max_length = 0
        if not split:
            return len(s)
        split = [-1] + split + [len(s)]
        i = 0
        while i < len(split) - 1:
            b = split[i] + 1
            e = split[i+1]
            max_length = max(max_length, self.longestSubstring(s[b:e], k))
            i += 1
        return max_length


if __name__ == '__main__':
    s = 'bbaaa'
    k = 3
    print s, k
    print Solution().longestSubstring(s, k)
