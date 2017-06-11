# coding: utf8

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        res = 0
        pre = 0
        cur = 0
        op = '+'
        s = s + '+'
        while i < len(s):
            if s[i] == ' ':
                pass
            elif s[i] not in '+-*/':
                cur = cur * 10 + int(s[i])
            else:
                cur_op = s[i]
                if op == '+':
                    res += pre
                    pre = cur
                elif op == '-':
                    res += pre
                    pre = 0 - cur
                elif op == '*':
                    pre = pre * cur
                else:
                    pre = int(float(pre) / cur)
                op = cur_op
                cur = 0
            i += 1
        res += pre
        return res


if __name__ == '__main__':
    s = '1+2*5/3+6/4*2'
    print s
    print Solution().calculate(s)
    s = '3+2*2'
    print s
    print Solution().calculate(s)
    s = '3+5/2'
    print s
    print Solution().calculate(s)
