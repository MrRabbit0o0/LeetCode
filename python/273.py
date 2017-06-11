# coding: utf8

class Solution(object):
    def __init__(self):
        self.english_number = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety',
        }

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        res = ''
        base = 10 ** 9
        for suffix in ('Billion', 'Million', 'Thousand', ''):
            a = self.small_number_to_words(num / base)
            if a != '#':
                res += a + ' ' + suffix + ' '
            num = num % base
            base /= 1000
        return res.strip()

    def small_number_to_words(self, num):
        if num == 0:
            return '#'
        if num in self.english_number:
            return self.english_number[num]
        a = num / 100
        b = num % 100
        res = ''
        if a != 0:
            res += self.english_number[a] + ' Hundred '
        if b != 0 and b in self.english_number:
            res += self.english_number[b]
        elif b!= 0:
            c = b % 10
            d = b - c
            res += self.english_number[d] + ' ' + self.english_number[c]
        return res.strip()


if __name__ == '__main__':
    for n in [0, 100, 1230000, 123456]:
        print n
        print Solution().numberToWords(n)
