# coding: utf8

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        base = 2 ** (n - 1)
        sub_code = self.grayCode(n-1)
        return sub_code + map(lambda x : x + base, sub_code[::-1])


if __name__ == '__main__':
    import random
    n = random.randint(1, 10)
    result = Solution().grayCode(n)
    for x in result:
        print '{:0{width}b}'.format(x, width=n)
