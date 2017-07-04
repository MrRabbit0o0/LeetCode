# coding: utf8

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        max_prodcut = 0
        aph = [set(w) for w in words]
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if not aph[i] & aph[j]:
                    max_prodcut = max(max_prodcut, len(words[i]) * len(words[j]))
        return max_prodcut

