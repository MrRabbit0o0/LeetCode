# coding: utf8

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        ones = 0
        m = 1
        while m <= n:
            ones += (n/m + 8) / 10 * m + (n/m % 10 == 1) * (n%m + 1)
            m *= 10
        return ones

if __name__ == '__main__':
    for n in [13, 20, 100, 110, -1]:
        print n
        print Solution().countDigitOne(n)

