# coding: utf8

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        min_price = prices[0]
        max_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            if price < min_price:
                max_profit = max(max_profit, max_price - min_price)
                min_price = price
                max_price = price
            elif price > max_price:
                max_price = price
        max_profit = max(max_profit, max_price - min_price)
        return max_profit

