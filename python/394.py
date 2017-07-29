# coding: utf8

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [['', 1]]
        num = ''
        for c in s:
            if c.isdigit():
                num += c
            elif c == '[':
                stack.append(['', int(num)])
                num = ''
            elif c == ']':
                sub, k = stack.pop()
                stack[-1][0] += sub * k
            else:
                stack[-1][0] += c
        return stack[0][0]


