# coding: utf8

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        T = {}
        def subP(b, e):
            if b == e:
                return True
            if s[b:e] in T:
                return T[s[b:e]]
            for i in range(b, e):
                if s[b:i+1] in wordDict:
                    if subP(i+1, e):
                        T[s[b:e]] = True
                        return True
            T[s[b:e]] = False
            return False
        return subP(0, len(s))


if __name__ == '__main__':
    s = 'leetcode'
    wordDict = ['leet', 'code']
    print Solution().wordBreak(s, wordDict)
    s = 'a'
    wordDict = []
    print Solution().wordBreak(s, wordDict)
