# coding: utf8

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        def subP(n):
            if n == m/2:
                return
            idx = 0
            while idx < m - 2*n-1:
                i1, j1 = n, n + idx
                i2, j2 = n + idx, m - n - 1
                i3, j3 = m - n - 1, m - n - idx - 1
                i4, j4 = m - n - idx - 1, n
                tmp = matrix[i4][j4]
                matrix[i4][j4] = matrix[i3][j3]
                matrix[i3][j3] = matrix[i2][j2]
                matrix[i2][j2] = matrix[i1][j1]
                matrix[i1][j1] = tmp
                idx += 1
            subP(n+1)
        subP(0)


if __name__ == '__main__':
    matrix = [[1,2],[4,3]]
    print matrix
    Solution().rotate(matrix)
    print matrix
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print matrix
    Solution().rotate(matrix)
    print matrix
