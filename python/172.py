# coding: utf8

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if n < 5 else n / 5 + self.trailingZeroes(n/5)


if __name__ == '__main__':
    import random
    n = random.randint(0, 10000000)
    print n
    print Solution().trailingZeroes(n)
    n = 7425429
    result = Solution().trailingZeroes(n)
    assert(1856353 == result), 'n={}, right=1856353, output={}'.format(n, result)
