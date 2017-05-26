# coding: utf8

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        m = len(board)
        n = len(board[0])
        if m < 3 or n < 3:
            return
        o_list = []
        o_pos = set()
        seed_list = []
        for j in range(n):
            if board[0][j] == 'O':
                seed_list.append((0, j))
            if board[m-1][j] == 'O':
                seed_list.append((m-1, j))

        for i in range(1, m-1):
            if board[i][0] == 'O':
                seed_list.append((i, 0))
            if board[i][n-1] == 'O':
               seed_list.append((i, n-1))

        while seed_list:
            x, y = seed_list.pop()
            if board[x][y] == 'O':
                if (x, y) in o_pos:
                    continue
                else:
                    o_pos.add((x, y))
                    if x > 0:
                        seed_list.append((x-1, y))
                    if x < m - 1:
                        seed_list.append((x + 1, y))
                    if y > 0:
                        seed_list.append((x, y - 1))
                    if y < n - 1:
                        seed_list.append((x, y + 1))

        for i in range(m):
            for j in range(n):
                if (i, j) not in o_pos:
                    board[i][j] = 'X'



if __name__ == '__main__':
    board = ["XXXX","XOOX","XXOX","XOXX"]
    board = map(list, board)
    Solution().solve(board)
    print board
