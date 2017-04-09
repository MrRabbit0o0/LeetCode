# coding: utf8

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n == 1:
            return 1
        if n < 4:
            return 0
        # every row or column must have a Queen
        grid = []
        solutions = []
        self.addQ(solutions, grid, n, 0)
        return len(solutions)

    def addQ(self, solutions, grid, n, ith):
        if ith == n:
            solutions.append([l for l in grid])
            return
        grid.append(None)
        for i in range(n):
            grid[ith] = i
            if self.isValid(grid, ith, i):
                self.addQ(solutions, grid, n, ith+1)
        grid.pop(ith)


    def isValid(self, grid, i, j):
        pos_list = []
        for e_i, e_j in enumerate(grid[:i]):
            if e_j == j:
                return False
            if abs(i - e_i) == abs(j - e_j):
                return False
        return True


if __name__ == '__main__':
    n = 9
    print n
    print Solution().solveNQueens(n)
