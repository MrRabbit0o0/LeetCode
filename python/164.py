# coding: utf8

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        new_nums = self.rdx_sort(nums)
        return max([new_nums[i+1] - new_nums[i] for i in range(len(nums)-1)])

    def rdx_sort(self, nums):
        i = 1
        num_list = map(str, nums)
        while True:
            finish_flag = True
            T = {k:[] for k in '0123456789'}
            for str_n in num_list:
                if len(str_n) < i:
                    key = '0'
                else:
                    finish_flag = False
                    key = str_n[-i]
                T[key].append(str_n)
            if finish_flag:
                break
            new_num_list = []
            for k in '0123456789':
                new_num_list += T[k]
            num_list = new_num_list
            i += 1
        return map(int, num_list)


if __name__ == '__main__':
    nums = [1, 4, 8, 29, 24, 15, 27]
    print nums
    #print Solution().maximumGap(nums)
    nums = [100, 3, 2, 1]
    print nums
    print Solution().maximumGap(nums)
