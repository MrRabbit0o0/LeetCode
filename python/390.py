# coding: utf8


class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        head = 1
        step = 1
        while n > 1:
            if left or n % 2 == 1:
                head = head + step
            n = n / 2
            step = step * 2
            left = left ^ 1
        return head

if __name__ == '__main__':
    n = 10000
    print Solution().lastRemaining(n)

