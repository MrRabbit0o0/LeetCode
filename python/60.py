# coding: utf8

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n < 1:
            return ''
        l = range(1, n+1)
        def subP(l, n, k):
            if n == 1 or k == 0:
                return l
            cum = reduce(lambda x, y: x*y, range(1, n))
            i = 0
            while i < n:
                if cum * i > k:
                    break
                i += 1
            i -= 1
            if i == n:
                l.reverse()
                return l
            else:
                new_l = l[:i] + l[i+1:]
                return [l[i]] + subP(new_l, n-1, k - cum * i)
        return ''.join(map(str, subP(l, n, k-1)))


if __name__ == '__main__':
    n = 3
    k = 3
    print Solution().getPermutation(n, k)

