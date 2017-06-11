# coding: utf8

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [0] * (m+1)
        max_l = 0
        pre = 0
        for j in range(0, n):
            for i in range(1, m+1):
                tmp = dp[i]
                if matrix[i-1][j] == '1':
                    dp[i] = min(dp[i], min(dp[i-1], pre)) + 1
                    max_l = max(max_l, dp[i])
                else:
                    dp[i] = 0
                pre = tmp

        return max_l ** 2


if __name__ == '__main__':
    matrix = ["10100","10111","11111","10010"]
    print matrix
    matrix = map(lambda x: [c for c in x], matrix)
    print Solution().maximalSquare(matrix)
    matrix = ["0001","1101","1111","0111","0111"]
    print matrix
    matrix = map(lambda x: [c for c in x], matrix)
    print Solution().maximalSquare(matrix)
