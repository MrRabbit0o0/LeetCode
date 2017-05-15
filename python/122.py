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
        for i in range(1, len(prices)):
            if prices[i] < prices[i-1]:
                min_price = prices[i]
            else:
                max_price = prices[i]
            if prices[i] >= prices[i-1] and (i == len(prices) - 1 or prices[i] > prices[i+1]):
                max_profit += max_price - min_price
        return max_profit


if __name__ == '__main__':
    prices = [1, 2, 3, 7, 4, 2, 1, 8, 9]
    print prices
    print Solution().maxProfit(prices)
    prices = [1, 2]
    print prices
    print Solution().maxProfit(prices)
