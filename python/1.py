class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        for i in range(len(nums)):
            key = nums[i]
            if key in hash:
                hash[key] = hash[key]+(i,)
            else:
                hash[key] = (i,)

        for k1, v1 in hash.items():
            k2 = target-k1
            if k2 in hash:
                if k2 != k1:
                    return [v1[0], hash[k2][0]]
                else:
                    if len(hash[k1]) == 2:
                        return [v1[0], v1[1]]

p = Solution()
print p.twoSum([3,2,4],6)