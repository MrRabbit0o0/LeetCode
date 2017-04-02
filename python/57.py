# coding: utf8
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        for i, inter in enumerate(intervals):
            if inter.start >= newInterval.start:
                new_intervals = intervals[:i] + [newInterval] + intervals[i:]
                return self.merge(new_intervals)
        new_intervals = intervals + [newInterval]
        return self.merge(new_intervals)


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
