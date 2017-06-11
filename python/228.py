# coding: utf8

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranges = []
        for n in nums:
            if not ranges or n > ranges[-1][-1] + 1:
                ranges.append([])
            if len(ranges[-1]) < 2:
                ranges[-1].append(n)
            else:
                ranges[-1][-1] = n
        return ['->'.join(map(str, s)) for s in ranges]


if __name__ == '__main__':
    nums = [0, 1, 2, 4, 5, 7]
    print nums
    print Solution().summaryRanges(nums)
