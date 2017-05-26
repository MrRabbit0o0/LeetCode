# coding: utf8

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = range(n+1)[1:]
        result = []
        def subP(pre, l, sub_k):
            if sub_k == 0:
                result.append(pre)
                return
            for i in range(len(l)-sub_k+1):
                subP(pre+[l[i]], l[i+1:], sub_k-1)
        subP([], nums, k)
        return result


if __name__ == '__main__':
    n = 4
    k = 2
    print n, k
    for x in Solution().combine(n, k):
        print x
