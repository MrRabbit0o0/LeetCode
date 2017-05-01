# coding: utf8

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == '0' or denominator == 0:
            return '0'
        result = ''
        if numerator * denominator < 0:
            result += '-'
        a = abs(numerator)
        b = abs(denominator)
        int_number = a / b
        result += str(int_number)
        if a % b == 0:
            return result
        else:
            result += '.'
        compute_record = {}
        rest = a % b

        while rest != 0:
            if rest in compute_record:
                idx = compute_record[rest]
                return result[:idx] + '(' + result[idx:] + ')'
            else:
                compute_record[rest] = len(result)
                rest *= 10
                r = rest / b
                rest = rest % b
                result += str(r)
        return result
