# coding: utf8

class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.origin_list = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.origin_list

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        tmp = [x for x in self.origin_list]
        random.shuffle(tmp)
        return tmp


