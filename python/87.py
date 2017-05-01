# coding: utf8


class Solution(object):
    T = {}
    def isScramble(self, s1, s2):
        import string
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if (s1, s2) in self.T:
            return self.T[(s1, s2)]
        if s1 == s2:
            self.T[(s1, s2)] = True
            return True
        if sorted(s1) != sorted(s2):
            self.T[(s1, s2)] = False
            return False
        for i in range(len(s1)-1):
            if self.isScramble(s1[:i+1], s2[:i+1]) and self.isScramble(s1[i+1:], s2[i+1:]):
                self.T[(s1, s2)] = True
                return True
            if self.isScramble(s1[:i+1], s2[-i-1:]) and self.isScramble(s1[i+1:], s2[:-i-1]):
                self.T[(s1, s2)] = True
                return True
        self.T[(s1, s2)] = False
        return False


if __name__ == '__main__':
    s1 = 'eat'
    s2 = 'tea'
    print Solution().isScramble(s1, s2)
    s1 = "abcdefghijklmn"
    s2 = "efghijklmncadb"
    print Solution().isScramble(s1, s2)
