# coding: utf8

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        T = [0] * len(t)
        T = [1] + T
        for c in s:
            for i in range(len(t)-1, -1, -1):
                if t[i] == c:
                    T[i+1] += T[i]
        return T[-1]


if __name__ == '__main__':
    s = 'aabb'
    t = 'ab'
    print s, t
    print Solution().numDistinct(s, t)

    s = 'ccc'
    t = 'cc'
    print s, t
    print Solution().numDistinct(s, t)

    s = "anacondastreetracecar"
    t = "contra"
    print s, t
    print Solution().numDistinct(s, t)

    s = "aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe"
    t = "bddabdcae"
    print s, t
    print Solution().numDistinct(s, t)
