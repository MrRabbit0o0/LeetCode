class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            high = self.__highest_number(x)
            low = 1
            while low < high:
                if (x / (10 ** (low-1))) % 10 == (x / (10 ** (high-1))) % 10:
                    low += 1
                    high -= 1
                else:
                    return False
            return True

    def __highest_number(self, x):
        count = 1
        while x >= 10:
            x /= 10
            count += 1
        return count

s = Solution()
print s.isPalindrome(10)
