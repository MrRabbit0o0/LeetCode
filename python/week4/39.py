import bisect


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ret = self.__find_sum(candidates, target)
        return ret

    def __find_sum(self, candidates, target):
        ret = []
        if target >= candidates[0]:
            target_index = bisect.bisect_left(candidates, target, 0, len(candidates))
            if target_index != len(candidates) and candidates[target_index] == target:
                ret.append([target])

            for index, item in enumerate(candidates):
                sum_list = self.__find_sum(candidates[index:], target - item)
                if sum_list:
                    for sub_list in sum_list:
                        sub_list.append(item)
                    ret.extend(sum_list)
        return ret


s = Solution()
print s.combinationSum([2, 3, 6, 7], 7)
