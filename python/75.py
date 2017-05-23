# coding: utf8

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def partition(l, p, q):
            pivot = l[q]
            i = p - 1
            for j in range(p, q):
                if l[j] <= pivot:
                    i += 1
                    l[i], l[j] = l[j], l[i]
            i += 1
            l[i], l[q] = l[q], l[i]
            return i

        def quicksort(l, p, q):
            if p < q:
                m = partition(l, p, q)
                quicksort(l, p, m-1)
                quicksort(l, m+1, q)
        quicksort(nums, 0, len(nums)-1)

if __name__ == '__main__':
    import random
    t = range(10)
    random.shuffle(t)
    print t
    Solution().sortColors(t)
    print t
