# coding: utf8

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        def remove(sub_s, last_i, last_j, par):
            stack = 0
            for i in range(last_i, len(sub_s)):
                if sub_s[i] == par[0]:
                    stack += 1
                elif sub_s[i] == par[1]:
                    stack -= 1
                if stack >=0:
                    continue
                for j in range(last_j, i+1):
                    if sub_s[j] == par[1] and (j == last_j or sub_s[j-1] != par[1]):
                        remove(sub_s[:j] + sub_s[j+1:], i, j, par)
                return
            reversed = sub_s[::-1]
            if par[0] == '(':
                remove(reversed, 0, 0, (')', '('))
            else:
                res.append(reversed)
        remove(s, 0, 0, ('(', ')'))
        return res


if __name__ == '__main__':
    s = "()())()"
    print Solution().removeInvalidParentheses(s)

