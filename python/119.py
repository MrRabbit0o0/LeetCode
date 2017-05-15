# coding: utf8

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return []
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        rowIndex -= 1
        last = [1, 1]
        while rowIndex > 0:
            new_line = [1] + map(lambda i : last[i] + last[i+1], range(len(last)-1)) + [1]
            last = new_line
            rowIndex -= 1
        return last


if __name__ == '__main__':
    rowIndex = 10
    print Solution().getRow(rowIndex)
