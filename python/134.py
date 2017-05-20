# coding: utf8

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start = len(gas) - 1
        end = 0
        cum = gas[start] - cost[start]
        while start > end:
            if cum >= 0:
                cum = gas[end] - cost[end]
                end += 1
            else:
                start -= 1
                cum = gas[start] - cost[start]
        return start if cum >= 0 else -1


if __name__ == '__main__':
    gas = [6,1,4,3,5]
    cost = [3,8,2,4,2]
    print gas
    print cost
    print Solution().canCompleteCircuit(gas, cost)
