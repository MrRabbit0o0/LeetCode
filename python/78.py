# coding: utf8

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        def subP(pre, l, sub_k):
            if sub_k == 0:
                result.append(pre)
                return
            for i in range(len(l)-sub_k+1):
                subP(pre+[l[i]], l[i+1:], sub_k-1)
        for k in range(len(nums), 0, -1):
            subP([], nums, k)
        return result

    def subsets2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result_nums = 2 ** len(nums)
        result = [[] for _ in range(result_nums)]
        for i in range(len(nums)):
            for j in range(result_nums):
                if j >> i & 1:
                    result[j].append(nums[i])
        return result


if __name__ == '__main__':
    nums = [1, 2, 3]
    for x in Solution().subsets2(nums):
        print x
