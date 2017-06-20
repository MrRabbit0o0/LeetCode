# coding: utf8

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length <= 1:
            return 0
        s0, s1, s2  = [0] * length, [0] * length, [0] * length
        s0[0] = 0
        s1[0] = -prices[0]
        s2[0] = None
        for i in range(1, length):
            s0[i] = max(s0[i-1], s2[i-1])
            s1[i] = max(s1[i-1], s0[i-1]-prices[i])
            s2[i] = s1[i-1] + prices[i]
        return max(s0[-1], s2[-1])


