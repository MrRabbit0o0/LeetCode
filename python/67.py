# coding: utf8

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ''
        if len(a) < len(b):
            a, b = b, a
        i = 1
        last = 0
        while i <= len(a):
            ac = int(a[-i])
            bc = int(b[-i]) if i <= len(b) else 0
            c = ac + bc + last
            last = c / 2
            c = c % 2
            result = str(c) + result
            i += 1
        return result if last == 0 else '1'+result


if __name__ == '__main__':
    a = '1001'
    b = '11'
    print a, b
    print Solution().addBinary(a, b)
