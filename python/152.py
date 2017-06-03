# coding: utf8

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # more fast
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        max_prod = nums[0]
        prod_cum = nums[0]
        for i in range(len(nums)):
            if nums[i] == 0:
                return max(0, max(self.maxProduct(nums[:i]), self.maxProduct(nums[i+1:])))
        negative_list = [i for i in range(len(nums)) if nums[i] < 0]
        if len(negative_list) % 2 == 0:
            return reduce(lambda x, y: x * y, nums)
        else:
            max1 = self.maxProduct(nums[:negative_list[0]])
            max2 = self.maxProduct(nums[negative_list[0]+1:])

            max3 = self.maxProduct(nums[:negative_list[-1]])
            max4 = self.maxProduct(nums[negative_list[-1]+1:])
            return max(max(max1, max2), max(max3, max4))

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_herepre = nums[0]
        min_herepre = nums[0]
        max_sofar = nums[0]
        for n in nums:
            max_here = max(max(max_herepre * n, min_herepre * n), n)
            min_here = min(min(max_herepre * n, min_herepre * n), n)
            max_sofar = max(max_sofar, max_here)
            max_herepre = max_here
            min_herepre = min_here
        return max_sofar

if __name__ == '__main__':
    nums = [2, 3, -1, 4, -1, -80]
    print Solution().maxProduct(nums)
