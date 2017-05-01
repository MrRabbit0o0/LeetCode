# coding: utf8

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = set()
        def subP(nums):
            if not nums:
                result.add(())
                return
            if tuple(nums) in result:
                return
            result.add(tuple(nums))
            i = 1
            last = nums[0]
            subP(nums[1:])
            while i < len(nums):
                if nums[i] != last:
                    subP(nums[:i]+nums[i+1:])
                    last = nums[i]
                i += 1
        nums.sort()
        subP(nums)
        return map(list, result)


if __name__ == '__main__':
    nums = [1, 2, 2]
    result = Solution().subsetsWithDup(nums)
    result.sort(reverse=True)
    for x in result:
        print x
