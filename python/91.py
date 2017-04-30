# coding: utf8

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        T = [-1] * len(s)
        def subP(i):
            sub_s = s[i:]
            if not sub_s:
                return 1
            if sub_s[0] == '0':
                return 0
            if len(sub_s) == 1 or sub_s == '10' or sub_s == '20':
                return 1
            if T[i] != -1:
                return T[i]
            n = int(sub_s[:2])
            if n > 26:
                count = subP(i+1)
            else:
                count = subP(i+1) + subP(i+2)
            T[i] = count
            return count

        return subP(0)


if __name__ == '__main__':
    s = '00'
    print s
    print Solution().numDecodings(s)
    s = '100'
    print s
    print Solution().numDecodings(s)
    s = '227'
    print s
    print Solution().numDecodings(s)

