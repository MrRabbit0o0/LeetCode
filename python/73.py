# coding: utf8

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        m = len(matrix)
        n = len(matrix[0])
        zero_idx = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_idx.append((i, j))
        rows = set([x[0] for x in zero_idx])
        columns = set([x[1] for x in zero_idx])
        for i in range(m):
            for j in range(n):
                if i in rows or j in columns:
                    matrix[i][j] = 0

