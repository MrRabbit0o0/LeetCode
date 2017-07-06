# coding: utf8

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [None] * (amount + 1)
        dp[0] = 0
        coins.sort()
        def subP(total):
            if total == 0:
                return 0
            if dp[total]:
                return dp[total]
            min_number = total + 1
            for n in coins:
                if n <= total:
                    cur = 1 + subP(total-n)
                    if cur > 0:
                        min_number = min(min_number, cur)
            if min_number == total + 1:
                min_number = -1
            dp[total] = min_number
            return dp[total]
        return subP(amount)


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 100
    print Solution().coinChange(coins, amount)
    coins = [186,419,83,408]
    amount = 6249
    print Solution().coinChange(coins, amount)

