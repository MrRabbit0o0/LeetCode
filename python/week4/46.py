class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        self.__generate_nums(set(nums), [], len(nums), ret)
        return ret

    def __generate_nums(self, nums, temp, length, ret):
        if len(temp) == length:
            ret.append(temp[:])
        else:
            for value in set(nums):
                temp.append(value)
                nums.remove(value)
                self.__generate_nums(nums, temp, length, ret)
                temp.pop()
                nums.add(value)


s = Solution()
print s.permute([1, 2, 3])
