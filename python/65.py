# coding: utf8

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            float(s)
        except:
            return False
        return True


if __name__ == '__main__':
    s = '  -2'
    print s
    print Solution().isNumber(s)
