# coding: utf8

class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        result = []
        def dfs(sub_num, pre, oprand, op, cum):
            if sub_num == '' and cum == target:
                result.append(pre)
                return
            for i in range(len(sub_num)):
                num_a = sub_num[:i+1]
                if num_a != str(int(num_a)):
                    continue
                a = int(num_a)
                # +
                dfs(sub_num[i+1:], pre + '+' + num_a, a, '+', cum + a)
                # -
                dfs(sub_num[i+1:], pre + '-' + num_a, a, '-', cum - a)
                # *
                if op == '+':
                    dfs(sub_num[i+1:], pre + '*' + num_a, a * oprand, op, cum - oprand  + oprand * a)
                elif op == '-':
                    dfs(sub_num[i+1:], pre + '*' + num_a, a * oprand, op, cum + oprand - oprand * a)
                else:
                    dfs(sub_num[i+1:], pre + '*' + num_a, a * oprand, op, a * oprand)

        if not num:
            return result
        for i in range(len(num)):
            s = num[:i+1]
            if s != str(int(s)):
                continue
            dfs(num[i+1:], s, int(s), '#', int(s))
        return result


if __name__ == '__main__':
    num = '123456789'
    target = 45
    print num, target
    for r in Solution().addOperators(num, target):
        print r

    num = '105'
    target = 5
    print num, target
    for r in Solution().addOperators(num, target):
