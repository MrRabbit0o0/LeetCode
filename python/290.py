# coding: utf8

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_list = str.split()
        if len(pattern) != len(str_list):
            return False
        p_map = {}
        dup_set = set()
        for i in range(len(pattern)):
            p = pattern[i]
            if p not in p_map:
                if str_list[i] in dup_set:
                    return False
                p_map[p] = str_list[i]
                dup_set.add(str_list[i])
            elif p_map[p] != str_list[i]:
                return False
        return True


if __name__ == '__main__':
    pattern = 'abba'
    str = 'dog cat cat dog'
    print Solution().wordPattern(pattern, str)

