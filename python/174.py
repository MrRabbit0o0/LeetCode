# coding: utf8

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon or not dungeon[0]:
            return 1
        m = len(dungeon)
        n = len(dungeon[0])
        T = [[100000] * (n + 1) for _ in range(m+1)]
        T[m-1][n] = T[m][n-1] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                need = min(T[i+1][j], T[i][j+1]) - dungeon[i][j]
                T[i][j] = need if need > 0 else 1
        return T[0][0]

if __name__ == '__main__':
    dungeon = [[0]]
    print Solution().calculateMinimumHP(dungeon)
