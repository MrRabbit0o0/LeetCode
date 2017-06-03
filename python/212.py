# coding: utf8


class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children.setdefault(c, TrieNode())
        node.isWord = True


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0]:
            return []
        trie = Trie()
        node = trie.root
        for word in words:
            trie.insert(word)
        m = len(board)
        n = len(board[0])
        result = []
        for i in range(m):
            for j in range(n):
                self.dfs(board, i, j, '', result, node)
        return result

    def dfs(self, board, i, j, pre, res, node):
        if node.isWord:
            res.append(pre)
            node.isWord = None
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] == '_':
            return
        pre += board[i][j]
        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node:
            return
        board[i][j] = '_'
        self.dfs(board, i-1, j, pre, res, node)
        self.dfs(board, i, j-1, pre, res, node)
        self.dfs(board, i+1, j, pre, res, node)
        self.dfs(board, i, j+1, pre, res, node)
        board[i][j] = tmp


if __name__ == '__main__':
    board = ["oaan","etae","ihkr","iflv"]
    words = ["oath","pea","eat","rain"]
    board = map(lambda x: [c for c in x], board)
    print Solution().findWords(board, words)
    board = ["aa"]
    words = ["aaa"]
    board = map(lambda x: [c for c in x], board)
    print Solution().findWords(board, words)
