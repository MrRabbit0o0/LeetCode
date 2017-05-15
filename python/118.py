# coding: utf8

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <=0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        numRows -= 2
        result = [[1], [1, 1]]
        while numRows > 0:
            last = result[-1]
            new_line = [1] + map(lambda i : last[i] + last[i+1], range(len(last)-1)) + [1]
            result.append(new_line)
            numRows -= 1
        return result


if __name__ == '__main__':
    numRows = 5
    for line in Solution().generate(numRows):
        print line
