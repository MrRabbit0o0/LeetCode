# coding: utf8

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = len(nums)
        if m <= 1:
            return 0
        step = 0
        c_max = 0
        i = 0
        n_max = 0
        while c_max - i + 1 > 0:
            step += 1
            while i <= c_max:
                n_max = max(n_max, nums[i]+i)
                if n_max >= m-1:
                    return step
                i += 1
            c_max = max(n_max, c_max)
        return 0




if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    print nums
    print Solution().jump(nums)
