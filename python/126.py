# coding: utf8

import string

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        set1 = set([beginWord])
        set2 = set([endWord])
        w_d = set(wordList)
        if endWord not in w_d:
            return []

        T = {}
        self.helper(w_d, set1, set2, T, False)
        res = []
        self.generate_list(beginWord, endWord, T, [beginWord], res)
        return res

    def helper(self, w_d, set1, set2, T, flip):
        if not set1:
            return False
        if len(set1) > len(set2):
            return self.helper(w_d, set2, set1, T, not flip)
        w_d = w_d - set1 - set2
        done = False
        set3 = set()

        for w in set1:
            for i in range(len(w)):
                for c in string.lowercase:
                    if c == w[i]:
                        continue
                    new_w = w[:i] + c + w[i+1:]
                    if flip:
                        key, val = new_w, w
                    else:
                        key, val = w, new_w
                    l = T.get(key, [])
                    if new_w in set2:
                        done = True
                        l.append(val)
                        T[key] = l
                    if not done and new_w in w_d:
                        set3.add(new_w)
                        l.append(val)
                        T[key] = l
        return done or self.helper(w_d, set2, set3, T, not flip)

    def generate_list(self, begin, end, T, pre, res):
        if begin == end:
            res.append(pre)
            return res
        if begin not in T:
            return []
        for w in T[begin]:
            self.generate_list(w, end, T, pre + [w], res)


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print beginWord, endWord
    print wordList
    print 'Result:'
    for x in Solution().findLadders(beginWord, endWord, wordList):
        print x
