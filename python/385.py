# coding: utf8


class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        curr = None

        for r in range(len(s)):
            char = s[r]
            if char == '[':
                if curr:
                    stack.append(curr)
                curr = NestedInteger()
                l = r + 1
            elif char == ']':
                if s[l:r]:
                    curr.add(NestedInteger(int(s[l:r])))
                if stack:
                    pre_node = stack.pop()
                    pre_node.add(curr)
                    curr = pre_node
                l = r + 1
            elif char == ',':
                if s[l-1] != ']':
                    num = int(s[l:r])
                    curr.add(NestedInteger(int(s[l:r])))
                l = r + 1
        return curr

    def deserialize(self, s):
        # reverse
        def subP():
            num = ''
            while s and s[-1] not in '[],':
                num += s.pop()
            if num:
                return NestedInteger(int(num))
            s.pop()
            lst = NestedInteger()
            while s[-1] != ']':
                lst.add(subP())
                if s[-1] == ',':
                    s.pop()
            s.pop()
            return lst
        s = list(s[::-1])
        return subP()


