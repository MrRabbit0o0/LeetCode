# coding: utf8

class Solution(object):
    def generateMatrix(self, m):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * m for _ in range(m)]
        n = 0
        num = 1
        while n != m/2:
            i = n
            j = n
            while j < m - n:
                matrix[i][j] = num
                num += 1
                j += 1
            j -= 1
            i += 1
            while i < m - n:
                matrix[i][j] = num
                num += 1
                i += 1
            j -= 1
            i -= 1
            while j >= n:
                matrix[i][j] = num
                num += 1
                j -= 1
            j += 1
            i -= 1
            while i > n:
                matrix[i][j] = num
                num += 1
                i -= 1
            n += 1

        if m % 2 == 1:
            matrix[m/2][m/2] = num
        return matrix

if __name__ == '__main__':
    for n in range(1, 6):
        result = Solution().generateMatrix(n)
        for x in result:
            print x
        print
