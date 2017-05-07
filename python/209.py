# coding: utf8

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_idx = {}
        for i in range(len(nums)):
            n = nums[i]
            if n not in num_idx:
                num_idx[n] = []
            for idx in num_idx[n]:
                if i - idx <= k:
                    return True
            num_idx[n].append(i)
        return False


if __name__ == '__main__':
    nums = []
    k = 0
    print Solution().containsNearbyDuplicate(nums, k)
    nums = [-1, -1]
    k = 1
    print Solution().containsNearbyDuplicate(nums, k)

