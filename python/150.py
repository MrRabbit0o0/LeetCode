# coding: utf8

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        op_map = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(1.0 * x / y),
        }
        num = []
        for op in tokens:
            if op not in '+-*/':
                num.append(int(op))
            else:
                b = num.pop(-1)
                a = num.pop(-1)
                c = op_map[op](a, b)
                num.append(c)
        return num[0]


if __name__ == '__main__':
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print tokens
    print Solution().evalRPN(tokens)
