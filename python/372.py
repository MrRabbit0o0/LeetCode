# coding: utf8

class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        if not b:
            return 1
        last = b.pop(-1)
        return self.powmod(self.superPow(a, b), 10) * self.powmod(a, last) % 1337

    def powmod(self, a, k):
        a = a % 1337
        return (a ** k) % 1337


if __name__ == '__main__':
    a = 2
    b = [3, 0, 0, 0, 0, 0, 0,0]
    print Solution().superPow(a, b)

