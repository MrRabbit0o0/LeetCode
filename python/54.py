# coding: utf8

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not all(matrix):
            return []
        if len(matrix) == 1:
            return matrix[0]
        elif len(matrix[0]) == 1:
            result = [x[0] for x in matrix]
            return result

        first_row = matrix[0]
        last_row = matrix[-1]

        matrix = matrix[1:-1]

        first_colum = [x[0] for x in matrix]
        last_colum = [x[-1] for x in matrix]

        last_row.reverse()
        first_colum.reverse()

        result = first_row + last_colum + last_row + first_colum

        matrix = [row[1:-1] for row in matrix]

        return result + self.spiralOrder(matrix)


if __name__ == '__main__':
    matrix = [[1,2],[4,3]]
    print matrix
    print Solution().spiralOrder(matrix)
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print matrix
    print Solution().spiralOrder(matrix)
    matrix = [[1,2,3],[4,5,6]]
    print matrix
    print Solution().spiralOrder(matrix)
