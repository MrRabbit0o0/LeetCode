# coding: utf8

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = [[0] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.matrix[i].append(self.matrix[i][-1] + matrix[i][j])

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return sum([self.matrix[row][col2+1] - self.matrix[row][col1] for row in range(row1, row2+1)])


