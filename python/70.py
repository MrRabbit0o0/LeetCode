# coding: utf8

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        T = [0] * (n + 1)
        T[0] = T[1] = 1
        def subP(i):
            if T[i] == 0:
                T[i] = subP(i-1) + subP(i-2)
            return T[i]
        return subP(n)

if __name__ == '__main__':
    import random
    n = random.randint(0, 20)
    print n
    print Solution().climbStairs(n)
