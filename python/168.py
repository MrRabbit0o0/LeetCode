# coding: utf8

class Solution(object):
    import string
    int2str = {k:v for k, v in zip(range(1, 27), string.uppercase)}
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 26:
            return self.int2str.get(n, '')
        else:
            idx = (n-1) / 26
            col = n - idx * 26
            res = self.int2str.get(col, '')
            return self.convertToTitle(idx) + res


if __name__ == '__main__':
    import random
    n = random.randint(0, 100)
    print n
    print Solution().convertToTitle(n)
    n =26
    print n
    print Solution().convertToTitle(n)
    n = 51
    print n
    print Solution().convertToTitle(n)
    n = 27
    print n
    print Solution().convertToTitle(n)
    n = random.randint(0, 100)
