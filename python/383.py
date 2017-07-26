# coding: utf8

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if not ransomNote:
            return True
        length = len(ransomNote)
        r_bucket = {}
        for c in ransomNote:
            r_bucket[c] = r_bucket.get(c, 0) + 1
        for c in magazine:
            if r_bucket.get(c, 0) > 0:
                r_bucket[c] -= 1
                length -= 1
            if length == 0:
                return True
        return False

