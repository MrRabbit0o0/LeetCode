# coding: utf8

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return [1]
        last = 1
        for i in range(len(digits)-1, -1, -1):
            tmp = digits[i] + last
            last = tmp / 10
            digits[i] = tmp % 10
            if last == 0:
                break
        if last == 1:
            digits = [last] + digits
        return digits


if __name__ == '__main__':
    import random
    digits = [random.randint(0, 9) for _ in xrange(random.randint(0, 100))]
    i = 0
    while i < len(digits):
        if digits[0] != 0:
            break
    print ''.join(map(str, digits))
    print ''.join(map(str, Solution().plusOne(digits)))
