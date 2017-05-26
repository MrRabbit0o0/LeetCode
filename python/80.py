# coding: utf8

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        last = None
        i = 0
        while i < len(nums):
            n = nums[i]
            if count == 0 or n != last:
                count = 1
                last = n
            elif count == 1:
                count += 1
            else:
                del nums[i]
                i -= 1
            i += 1
        return len(nums)


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    print nums
    print Solution().removeDuplicates(nums)
    print nums
