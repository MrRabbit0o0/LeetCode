# coding: utf8

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        a_num = 0
        secret_bucket = [0] * 10
        guess_bucket = [0] * 10
        for c1, c2 in zip(secret, guess):
            if c1 == c2:
                a_num += 1
            else:
                secret_bucket[int(c1)] += 1
                guess_bucket[int(c2)] += 1
        b_num = sum([min(a, b) for a, b in zip(secret_bucket, guess_bucket)])
        return '{}A{}B'.format(a_num, b_num)


if __name__ == '__main__':
    secret = '1134'
    guess = '0134'
    print Solution().getHint(secret, guess)

