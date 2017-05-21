# coding: utf8

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        flag = [1]
        last = '0'
        total = 0
        last_op = 1
        for c in s:
            if c == ' ':
                continue
            if c not in '+-()':
                last += c
            else:
                total += last_op * int(last)
                if c == '+':
                    last_op = flag[-1] * 1
                if c == '-':
                    last_op = flag[-1] * -1
                if c == '(':
                    flag.append(last_op)
                if c == ')':
                    flag.pop(-1)
                    last_op = flag[-1]
                last = '0'
        total += last_op * int(last)
        return total


if __name__ == '__main__':
    s = '(1-(4+(5-2))-3)-(6+8)'
    print s
    print Solution().calculate(s)
