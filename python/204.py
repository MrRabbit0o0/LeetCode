# coding: utf8

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            primes[i * i: n : i] = [False] * len(primes[i * i: n: i])

        return sum(primes)


if __name__ == '__main__':
    import random
    n = random.randint(0, 100000)
    n = 49979
    print n
    print Solution().countPrimes(n)
