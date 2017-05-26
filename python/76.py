# coding: utf8

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count = {}
        for c in t:
            count[c] = count.get(c, 0) + 1
        counter = len(t)
        result = ''
        begin = end = 0
        while end < len(s):
            if count.get(s[end], 0) > 0:
                counter -= 1
            count[s[end]] = count.get(s[end], -1) - 1
            while counter == 0:
                if result == '' or len(result) > (end - begin + 1):
                    result = s[begin:end+1]
                if count.get(s[begin], -1) == 0:
                    counter += 1
                count[s[begin]] += 1
                begin += 1
            end += 1
        return result


if __name__ == '__main__':
    s = 'ADOBECODEBANC'
    t = 'ABC'
    print s, t
    print Solution().minWindow(s, t)
    s = 'bba'
    t = 'ba'
    print s, t
    print Solution().minWindow(s, t)
