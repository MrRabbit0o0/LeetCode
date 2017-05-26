# coding: utf8

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0
        candy = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1
        for i in range(len(ratings)-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                candy[i-1] = max(candy[i]+1, candy[i-1])
        return sum(candy)


if __name__ == '__main__':
    ratings = [6,1,4,3,5]
    print ratings
    print Solution().candy(ratings)
    ratings = [1,4,4]
    print ratings
    print Solution().candy(ratings)
    ratings = [4,2,3,4,1]
    print ratings
    print Solution().candy(ratings)
    ratings = [1, 3, 4, 3, 2, 1]
    print ratings
    print Solution().candy(ratings)
