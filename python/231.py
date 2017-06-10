# coding: utf8

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and sum(map(lambda x: 1 if x == '1' else 0, bin(n)[2:])) == 1


if __name__ == '__main__':
    n = 1
    print n
    print Solution().isPowerOfTwo(n)
