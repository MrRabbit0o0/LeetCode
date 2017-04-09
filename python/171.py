# coding: utf8

class Solution(object):
    import string
    str2int = {v:k for k, v in zip(range(1, 27), string.uppercase)}
    def titleToNumber(self, s):
        """
        :type n: int
        :rtype: str
        """
        base = 0
        step = 1
        for x in s[::-1]:
            base += self.str2int.get(x, 0) * step
            step *= 26
        return base


if __name__ == '__main__':
    s = 'AAB'
    print s
    print Solution().titleToNumber(s)
