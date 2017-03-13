class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) == 0 or len(s) == 1 or numRows == 1:
            return s
        else:
            ret = ""
            columns = len(s) / (numRows*2-2)
            if len(s) % (numRows*2-2) != 0:
                columns += 1

            for i in range(numRows):
                for j in range(columns):
                    vertical = 2*j*(numRows-1)+i
                    edge = (2*j+2)*(numRows-1)-i
                    if vertical < len(s):
                        ret += s[vertical]
                    if edge < len(s) and i != 0 and i != numRows-1:
                        ret += s[edge]
            return ret

s = Solution()
print s.convert("ABC", 2)
