# coding: utf8

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                neighbor = 0
                if i  > 0:
                    neighbor += board[i-1][j-1] % 2 if j > 0 else 0
                    neighbor += board[i-1][j] % 2
                    neighbor += board[i-1][j+1] % 2 if j < n-1 else 0
                neighbor += board[i][j-1] % 2 if j > 0 else 0
                neighbor += board[i][j+1] % 2 if j < n-1 else 0
                if i < m - 1:
                    neighbor += board[i+1][j-1] % 2 if j > 0 else 0
                    neighbor += board[i+1][j] % 2
                    neighbor += board[i+1][j+1] % 2 if j < n-1 else 0
                if board[i][j] == 1 and neighbor not in (2, 3):
                    board[i][j] = 3
                elif board[i][j] == 0 and neighbor == 3:
                    board[i][j] = 2
        for i in range(m):
            for j in range(n):
                if board[i][j] == 3:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1


if __name__ == '__main__':
    board = [[1, 1], [1, 0]]
    print board
    Solution().gameOfLife(board)
    print board
