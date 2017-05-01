# coding: utf8

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        #return len(s) and len(s.split()) and len(s.split()[-1])
        if not s:
            return 0
        l_len = 0
        c_len = 0
        for x in s:
            if x != ' ':
                c_len += 1
            else:
                l_len = c_len if c_len != 0 else l_len
                c_len = 0
        return c_len if c_len != 0 else l_len


if __name__ == '__main__':
    s = ' '
    print s
    print Solution().lengthOfLastWord(s)
    s = ''
    print s
    print Solution().lengthOfLastWord(s)
    s = 'Hello World'
    print s
    print Solution().lengthOfLastWord(s)
    s = 'Hello World    '
    print s
    print Solution().lengthOfLastWord(s)
