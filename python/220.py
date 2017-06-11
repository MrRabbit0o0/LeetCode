# coding: utf8

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0:
            return False
        m = len(nums)
        bucket = {}
        w = t + 1
        for i in range(m):
            bucket_num = nums[i] / w
            if bucket_num in bucket:
                return True
            if bucket_num - 1 in bucket and nums[i] - bucket[bucket_num-1] <= t:
                return True
            if bucket_num + 1 in bucket and bucket[bucket_num+1] - nums[i] <= t:
                return True
            bucket[bucket_num] = nums[i]
            if i >= k:
                del bucket[nums[i-k] / w]

        return False
