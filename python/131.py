# coding: utf8

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        def subP(s, idx, pre):
            if idx == len(s):
                result.append(pre)
                return
            for i in range(idx, len(s)):
                l = idx
                r = i
                while l < r and s[l] == s[r]:
                    l += 1
                    r -= 1
                if l >= r:
                    subP(s, i+1, pre + [s[idx:i+1]])
        subP(s, 0, [])
        return result



if __name__ == '__main__':
    s = 'aab'
    for x in Solution().partition(s):
        print x
