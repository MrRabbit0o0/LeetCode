# coding: utf8

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        def travel(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
                return
            else:
                grid[i][j] = '0'
                map(travel, (i-1, i+1, i, i), (j, j, j-1, j+1))

        island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    travel(i, j)
                    island += 1
        return island

