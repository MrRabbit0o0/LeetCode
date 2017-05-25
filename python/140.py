# coding: utf8

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        word_dict = set(wordDict)
        T = {'':['']}
        def subP(sub_s):
            if sub_s in T:
                return T[sub_s]
            r_list = []
            for i in range(len(sub_s)):
                if sub_s[:i+1] in word_dict:
                    r = [sub_s[:i+1] + ' ' + suffix for suffix in subP(sub_s[i+1:])]
                    r_list += r
            T[sub_s] = r_list
            return r_list

        return map(lambda x: x.strip(), subP(s))


if __name__ == '__main__':
    s = 'catsanddog'
    wordDict = ['cat', 'cats', 'and', 'sand', 'dog']
    print Solution().wordBreak(s, wordDict)

