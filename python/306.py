# coding: utf8

class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        def subP(pre_a, pre_b, s):
            c = pre_a + pre_b
            if s == '':
                return False
            if s[0] == '0':
                return len(s) == 1 and pre_a + pre_b == 0
            if int(s) == c:
                return True
            prefix = str(c)
            if s[:len(prefix)] == prefix:
                return subP(pre_b, c, s[len(prefix):])
            else:
                return False

        if len(num) < 3:
            return False
        max_one = len(num) / 2
        max_i = 1 if num[0] == '0' else max_one
        for i in range(max_i):
            a = num[:i+1]
            max_j = 1 if num[i+1] == '0' else max_one
            start = i + 1
            for j in range(max_j):
                b = num[start:start+j+1]
                if subP(int(a), int(b), num[start+j+1:]):
                    return True
        return False



if __name__ == '__main__':
    for s in ['199111992', '023581', '12122436', '1203']:
        print s
        print Solution().isAdditiveNumber(s)
