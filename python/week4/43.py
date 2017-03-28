class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) < len(num2):
            return self.multiply(num2, num1)
        else:
            num2 = list(num2)
            num1 = list(num1)
            num1.reverse()
            num2.reverse()
            ret = []
            for count, multiplier in enumerate(num2):
                mul = self.__multiply(num1, multiplier)
                mul.extend(['0'] * count)
                ret = self.__add(ret, mul)
            return "".join(ret)

    def __multiply(self, num1, num2):
        ret = []
        multiplier = int(num2)
        if multiplier == 0:
            ret.append('0')
        elif multiplier == 1:
            ret.extend(num1)
        else:
            carry, remainder = 0, 0
            for multiplicand in num1:
                mul = multiplier * int(multiplicand)
                mul += carry
                carry, remainder = divmod(mul, 10)
                ret.append(str(remainder))
            if carry:
                ret.append(str(carry))
        ret.reverse()
        return ret

    def __add(self, num1, num2):
        ret = []
        carry = 0
        while num1 or num2 or carry:
            val1, val2 = 0, 0
            if num1:
                val1 = int(num1[-1])
            if num2:
                val2 = int(num2[-1])
            carry, remainder = divmod(val1 + val2 + carry, 10)
            ret.append(str(remainder))
            num1 = num1[:-1]
            num2 = num2[:-1]
        ret.reverse()
        return ret