# coding: utf8

class Solution(object):
    def __init__(self):
        self.binary_base = [2**i for i in range(32)]
        self.binary_base.reverse()

    def change2binary(self, num):
        binary_num = ''
        for base in self.binary_base:
            if num >= base:
                num -= base
                bit = '1'
            else:
                bit = '0'
            binary_num += bit
        return binary_num

    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        b_m = self.change2binary(m)
        b_n = self.change2binary(n)
        for i in range(32):
            if b_m[i] != b_n[i]:
                break
        else:
            return m
        return sum([self.binary_base[idx] for idx in range(i) if b_m[idx] == '1'])


    def rangeBitwiseAnd2(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        i = 0
        factor = 1
        while m != n:
            m >>= 1
            n >>= 1
            factor <<= 1
        return m * factor


if __name__ == '__main__':
    m_n = [5, 7]
    #m_n = [1, 1]
    print m_n
    print Solution().rangeBitwiseAnd(*m_n)

