import bisect


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        return self.__find_sum(candidates, target)

    def __find_sum(self, candidates, target):
        ret = []
        if candidates and target >= candidates[0]:
            length = len(candidates)
            target_index = bisect.bisect_left(candidates, target, 0, length)
            if target_index != length and candidates[target_index] == target:
                ret.append([target])

            if length > 1:
                pre_item = None
                for index, item in enumerate(candidates[:length - 1]):
                    if item != pre_item:
                        pre_item = item
                        sums = self.__find_sum(candidates[index + 1:], target - item)
                        if sums:
                            for one_sum in sums:
                                one_sum.append(item)
                            ret.extend(sums)
        return ret


s = Solution()
print s.combinationSum2(
    [14, 6, 25, 9, 30, 20, 33, 34, 28, 30, 16, 12, 31, 9, 9, 12, 34, 16, 25, 32, 8, 7, 30, 12, 33, 20, 21, 29, 24, 17,
     27, 34, 11, 17, 30, 6, 32, 21, 27, 17, 16, 8, 24, 12, 12, 28, 11, 33, 10, 32, 22, 13, 34, 18, 12]
    , 27)
