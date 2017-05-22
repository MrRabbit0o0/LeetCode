# coding: utf8

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = [0] * 26
        pos = 0
        for c in s:
            idx = ord(c) - ord('a')
            cnt[idx] += 1
        for i in range(len(s)):
            idx = ord(s[i]) - ord('a')
            if s[i] < s[pos]:
                pos = i
            cnt[idx] -= 1
            if cnt[idx] == 0:
                break
        if len(s) == 0:
            return ""
        else:
            return s[pos] + self.removeDuplicateLetters(s[pos+1:].replace(s[pos], ''))



if __name__ == '__main__':
    s = 'cbacdcbc'
    print s
    print Solution().removeDuplicateLetters(s)

