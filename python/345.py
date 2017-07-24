# coding: utf8


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        VOWELS = 'aeiou'
        index = []
        vowels = []
        for i, c in enumerate(s):
            if c.lower() in VOWELS:
                index.append(i)
                vowels.append(c)
        str_list = list(s)
        i = 0
        while i < len(str_list) and index:
            if i == index[0]:
                index.pop(0)
                str_list[i] = vowels.pop()
            i += 1
        return ''.join(str_list)



