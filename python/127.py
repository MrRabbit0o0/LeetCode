# coding: utf8

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        import string
        node_list = [beginWord]
        pool_list = set(wordList)
        depth = 0
        while node_list:
            depth += 1
            new_node_list = []
            for l in node_list:
                if l == endWord:
                    return depth
                for i in range(len(l)):
                    for c in string.lowercase:
                        new_l = l[:i] + c + l[i+1:]
                        if new_l in pool_list:
                            pool_list.remove(new_l)
                            new_node_list.append(new_l)
            node_list = new_node_list
        return 0


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print beginWord, endWord
    print wordList
    print Solution().ladderLength(beginWord, endWord, wordList)
