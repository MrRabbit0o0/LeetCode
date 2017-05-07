# coding: utf8

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = set()
        dup_set = set()
        for i in range(len(s) - 9):
            sub_s = s[i:i+10]
            if sub_s in dup_set:
                result.add(sub_s)
            else:
                dup_set.add(sub_s)
        return list(result)

