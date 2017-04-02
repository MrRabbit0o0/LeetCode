# coding: utf8
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals_sorted = sorted(intervals, key=lambda x: (x.start, x.end))
        i = 1
        m = len(intervals_sorted)
        last_s = intervals_sorted[0].start
        last_e = intervals_sorted[0].end
        result = []
        while i < m:
            inter = intervals_sorted[i]
            if inter.start <= last_e:
                last_e = max(inter.end, last_e)
            else:
                result.append(Interval(last_s, last_e))
                last_s = inter.start
                last_e = inter.end
            i += 1
        result.append(Interval(last_s, last_e))

        return result


if __name__ == '__main__':
    def test(test_case):
        intervals = []
        for s, e in test_case:
            intervals.append(Interval(s, e))
        print test_case
        result = Solution().merge(intervals)
        r_list = []
        for inter in result:
            r_list.append([inter.start, inter.end])
        print r_list

    test_case = [[3, 7]]
    test(test_case)
    test_case = [[1,5],[3, 7]]
    test(test_case)
    test_case = [[1,4],[2, 3]]
    test(test_case)
