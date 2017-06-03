# coding: utf8

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        result = ''.join(sorted(map(str, nums), cmp=lambda x, y: -1 if x+y > y+x else 1))
        i = 0
        while i < len(result) - 1:
            if result[i] != '0':
                break
            i += 1
        return result[i:]

    def largestNumber(self, nums):
        result = ''.join(sorted(map(str, nums), cmp=self.comp, reverse=True))
        i = 0
        while i < len(result) - 1:
            if result[i] != '0':
                break
            i += 1
        return result[i:]

    def comp(self, x, y):
        if x == y:
            return 0
        m = len(x)
        n = len(y)
        min_l = min(m, n)
        if x[:min_l] < y[:min_l]:
            return -1
        elif x[:min_l] > y[:min_l]:
            return 1
        else:
            if m < n:
                return self.comp(x[:min_l], y[min_l:])
            else:
                return self.comp(x[min_l:], y[:min_l])


if __name__ == '__main__':
    nums = [121, 12]
    print nums
    print Solution().largestNumber(nums)

    nums = [824, 8248]
    print nums
    print Solution().largestNumber(nums)
