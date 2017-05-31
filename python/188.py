# coding: utf8

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k < 1 or len(prices) < 2:
            return 0
        prices.append(0)
        stack = []
        if prices[0] < prices[1]:
            stack.append(prices[0])
        for i in range(1, len(prices)-1):
            if prices[i] > prices[i-1] and prices[i] >= prices[i+1]:
                stack.append(prices[i])
            elif prices[i] <= prices[i-1] and prices[i] < prices[i+1]:
                stack.append(prices[i])

        if len(stack) / 2 <= k:
            total = 0
            i = 0
            while i < len(stack) - 1:
                total += stack[i+1] - stack[i]
                i += 2
            return total

        hold_list = [-100000] * k
        release_list = [0] * k
        for p in prices:
            for i in range(k, 1, -1):
                release_list[i-1] = max(release_list[i-1], hold_list[i-1] + p)
                hold_list[i-1] = max(hold_list[i-1], release_list[i-1-1]-p)
            release_list[0] = max(release_list[0], hold_list[0] + p)
            hold_list[0] = max(hold_list[0], -p)
        return release_list[-1]

