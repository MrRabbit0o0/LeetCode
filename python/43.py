# coding: utf8

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1 = map(int, num1)
        n2 = map(int, num2)
        result = [0] * (len(n1) + len(n2))
        for j, b in enumerate(n2[::-1]):
            last = 0
            for i, a in enumerate(n1[::-1]):
                idx = - (i+j+1)
                c = result[idx]
                c += a * b + last
                last = c / 10
                c = c % 10
                result[idx] = c
            idx -= 1
            result[idx] += last
            if result[idx] > 9:
                result[idx-1] = 1
                result[idx] %= 10
        r_s = ''
        for x in result:
            if x == 0 and r_s == '':
                continue
            else:
                r_s += str(x)
        return r_s if r_s != '' else 0


if __name__ == '__main__':
    import random
    num1 = str(random.randint(0, 100000))
    num2 = str(random.randint(0, 10000))
    print num1, num2
    print int(num1) * int(num2)
    print Solution().multiply(num1, num2)
