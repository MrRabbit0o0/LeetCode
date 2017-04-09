# coding: utf8

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        uniq_dict = {}
        for x in strs:
            key = tuple(sorted([c for c in x]))
            uniq_dict[key] = uniq_dict.get(key, []) + [x]
        return uniq_dict.values()

if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    for line in Solution().groupAnagrams(strs):
        print line
