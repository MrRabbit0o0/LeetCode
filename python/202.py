# coding: utf8

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        try_times = 10
        number = n
        while try_times > 0:
            sum = 0
            for x in str(number):
                sum += int(x) ** 2
            if sum == 1:
                return True
            else:
                number = sum
            try_times -= 1
        return False


if __name__ == '__main__':
    import random
    n = random.randint(0, 10000000)
    print n
    print Solution().isHappy(n)
