# coding: utf8


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        hold1 = hold2 = -100000
        release1 = 0
        release2 = 0
        for x in prices:
            release2 = max(release2, hold2 + x)
            hold2 = max(hold2, release1 - x)
            release1 = max(release1, hold1 + x)
            hold1 = max(hold1, -x)
        return release2


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        max_profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] <= prices[i]:
                continue
            new_max = self.oneMax(prices[:i]) + self.oneMax(prices[i:])
            if new_max > max_profit:
                max_profit = new_max
        return max_profit


    def oneMax(self, prices):
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

