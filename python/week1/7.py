class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        digits = []
        if x > 0:
            symbol = 1
        else:
            symbol = -1

        x *= symbol
        while x > 0:
            digits.append(x % 10)
            x /= 10

        count = 0
        for i in range(len(digits)):
            if digits[i] == 0:
                count += 1
            else:
                break
        del digits[0:count]

        if len(digits) == 0:
            ret = 0
        elif len(digits) == 1:
            ret = digits[0]*symbol
        else:
            ret = reduce(lambda foo, bar: foo*10+bar, digits)
            if symbol == 1 and ret <= 2**31 - 1:
                pass
            elif symbol == -1 and ret <= 2**31:
                ret *= -1
            else:
                ret = 0
        return ret

s = Solution()
print s.reverse(1534236469)
