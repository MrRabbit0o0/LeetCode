# coding: utf8

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return word == ''
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    board[i][j] = '#'
                    result = self.search(board, word[1:], i, j)
                    board[i][j] = word[0]
                    if result:
                        return True
        return False

    def search(self, board, word, i, j):
        if not word:
            return True
        target = word[0]
        m = len(board)
        n = len(board[0])
        if i - 1 >= 0 and board[i-1][j] == target:
            board[i-1][j] = '#'
            result = self.search(board, word[1:], i-1, j)
            board[i-1][j] = target
            if result:
                return True
        if j - 1 >= 0 and board[i][j-1] == target:
            board[i][j-1] = '#'
            result = self.search(board, word[1:], i, j-1)
            board[i][j-1] = target
            if result:
                return True
        if i + 1 < m and board[i+1][j] == target:
            board[i+1][j] = '#'
            result = self.search(board, word[1:], i+1, j)
            board[i+1][j] = target
            if result:
                return True
        if j + 1 < n and board[i][j+1] == target:
            board[i][j+1] = '#'
            result = self.search(board, word[1:], i, j+1)
            board[i][j+1] = target
            if result:
                return True
        return False




if __name__ == '__main__':
    board = [['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E'],]
    word = 'ABCCED'
    print Solution().exist(board, word)
    word = 'SEE'
    print Solution().exist(board, word)
    word = 'ABCB'
    print Solution().exist(board, word)
