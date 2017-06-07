# coding: utf8

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        def subP(pre, k, n):
            if k == 0 and n == 0:
                res.append(pre)
                return
            min_idx = pre[-1]+1 if pre else 1
            for i in range(min_idx, 10):
                if i > n:
                    continue
                subP(pre + [i], k-1, n-i)
        subP([], k, n)
        return res


if __name__ == '__main__':
    k = 3
    n = 7
    print k, n
    print Solution().combinationSum3(k, n)
