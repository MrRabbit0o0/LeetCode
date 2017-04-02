# coding: utf8

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        said = [1]
        def say(s):
            thing = []
            idx = 0
            while idx < len(s):
                count = 0
                num = s[idx]
                while idx < len(s) and num == s[idx]:
                    count += 1
                    idx += 1
                thing.extend([count, num])
            return thing

        while n > 1:
            said = say(said)
            n -= 1
        return ''.join(map(str, said))



if __name__ == '__main__':
    for n in range(1, 10):
        print Solution().countAndSay(n)
