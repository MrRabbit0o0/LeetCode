# coding: utf8

import sys

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        index = [0] * len(primes)
        ugly = [sys.maxint] * n
        ugly[0] = 1
        for i in range(1, n):
            for j in range(len(primes)):
                ugly[i] = min(ugly[i], ugly[index[j]] * primes[j])
            for j in range(len(primes)):
                index[j] += 1 if ugly[i] == ugly[index[j]] * primes[j] else 0
        return ugly[-1]

