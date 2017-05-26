# coding: utf8

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        s = s.lower()
        lf = 0
        rt = len(s) - 1
        while lf < rt:
            if 'a' <= s[lf] <= 'z' or '0' <= s[lf] <= '9':
                if 'a' <= s[rt] <= 'z' or '0' <= s[rt] <= '9':
                    if s[lf] == s[rt]:
                        lf += 1
                        rt -= 1
                    else:
                        return False
                else:
                    rt -= 1
            else:
                lf += 1
        return True

if __name__ == '__main__':
    s = 'A man, a plan, a canal: Panama'
    print Solution().isPalindrome(s)
    s = 'race a car'
    print Solution().isPalindrome(s)

