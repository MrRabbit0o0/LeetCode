from collections import Counter


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        counter = dict(Counter(nums))
        ret = []
        self.__permute(counter, len(nums), ret, [])
        return ret

    def __permute(self, counter, length, ret, temp):
        if len(temp) == length:
            ret.append(temp[:])
        else:
            for key, value in dict(counter).items():
                temp.append(key)
                if value > 1:
                    counter[key] = value - 1
                else:
                    del counter[key]
                self.__permute(counter, length, ret, temp)
                temp.pop()
                counter[key] = value


s = Solution()
print s.permuteUnique([1, 1, 2])
