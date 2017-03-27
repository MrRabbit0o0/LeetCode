class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ret = ""
        while num != 0:
            result = self.int2RomanLetter(num)
            num = result[0]
            ret += result[1]
        return ret

    def int2RomanLetter(self, num):
        if num >= 1000:
            return num-1000, "M"
        elif num >= 900:
            return num-900, "CM"
        elif num >= 500:
            return num-500, "D"
        elif num >= 400:
            return num-400, "CD"
        elif num >= 100:
            return num-100, "C"
        elif num >= 90:
            return num-90, "XC"
        elif num >= 50:
            return num-50, "L"
        elif num >= 40:
            return num-40, "XL"
        elif num >= 10:
            return num-10, "X"
        elif num >= 9:
            return num-9, "IX"
        elif num >= 5:
            return num-5, "V"
        elif num >= 4:
            return num-4, "IV"
        else:
            return num-1, "I"


