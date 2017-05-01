# coding: utf8

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        def subP(pre, sub_s, i):
            length = len(sub_s)
            if length < i or length > i * 3:
                return
            if i == 1:
                if (sub_s[0] != '0' or sub_s == '0') and int(sub_s) <= 255:
                    result.append(pre + '.' + sub_s)
                return
            if 99 < int(sub_s[:3]) <= 255:
                subP(pre + '.' + sub_s[:3], sub_s[3:], i-1)
            subP(pre + '.' + sub_s[:1], sub_s[1:], i-1)
            if sub_s[0] != '0':
                subP(pre + '.' + sub_s[:2], sub_s[2:], i-1)
            return
        subP('', s, 4)
        return map(lambda x:x[1:], result)


if __name__ == '__main__':
    s = '0000'
    print s
    print Solution().restoreIpAddresses(s)
    s = '25525511135'
    print s
    print Solution().restoreIpAddresses(s)
    s = '010010'
    print s
    print Solution().restoreIpAddresses(s)
