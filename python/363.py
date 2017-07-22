# coding: utf8

import bisect

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        if not matrix or not matrix[0]:
            return None
        row = len(matrix)
        col = len(matrix[0])
        result = float('-inf')
        for l in range(col):
            sum_list = [0] * row
            for r in range(l, col):
                for i in range(row):
                    sum_list[i] += matrix[i][r]

                accu = [0]
                cur_max = float('-inf')
                cur_sum = 0
                for s in sum_list:
                    cur_sum += s
                    val = bisect.bisect_left(accu, cur_sum - k)
                    if val < len(accu):
                        cur_max = max(cur_max, cur_sum - accu[val])
                    bisect.insort(accu, cur_sum)
                result = max(cur_max, result)
        return result


if __name__ == '__main__':
    matrix = [[2,2,-1]]
    k = 2
    print matrix
    print Solution().maxSumSubmatrix(matrix, k)
