# coding: utf8

def p(t):
    print [(x.start, x.end) for x in t]

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class SummaryRanges(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.interval_list = []

    def binarySearch(self, val, lf, rt):
        if lf == rt:
            return -1
        if lf + 1 == rt and self.interval_list[lf].start < val:
            return lf
        mid = (lf + rt) / 2
        if self.interval_list[mid].start == val:
            return mid
        elif self.interval_list[mid].start > val:
            return self.binarySearch(val, lf, mid)
        else:
            return self.binarySearch(val, mid, rt)

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        idx = self.binarySearch(val, 0, len(self.interval_list))
        if idx != -1 and self.interval_list[idx].end >= val:
            return
        if idx != len(self.interval_list) - 1 and val + 1 == self.interval_list[idx+1].start:
            self.interval_list[idx+1].start = val
        elif idx != -1 and self.interval_list[idx].end + 1 == val:
            self.interval_list[idx].end = val
            return
        else:
            self.interval_list = self.interval_list[:idx+1] \
                                 + [Interval(val, val)] + self.interval_list[idx+1:]
        if idx != -1 and self.interval_list[idx].end + 1 == self.interval_list[idx+1].start:
            self.interval_list[idx].end = self.interval_list[idx+1].end
            self.interval_list.pop(idx+1)

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.interval_list


if __name__ == '__main__':

    sol = SummaryRanges()
    sol.addNum(1)
    p(sol.getIntervals())
    sol.addNum(3)
    p(sol.getIntervals())
    sol.addNum(7)
    p(sol.getIntervals())
    sol.addNum(2)
    p(sol.getIntervals())
    sol.addNum(6)
    p(sol.getIntervals())

    sol.addNum(9)
    p(sol.getIntervals())
    sol.addNum(4)
    p(sol.getIntervals())

    sol.addNum(10)
    p(sol.getIntervals())
    sol.addNum(5)
    p(sol.getIntervals())
