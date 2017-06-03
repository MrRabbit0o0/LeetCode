# coding: utf8

class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        tree = self.tree
        for c in word:
            if c not in tree:
                tree[c] = {}
            tree = tree[c]
        tree['end'] = None

    def search(self, word):
        """
        Returns if the word is in the data structure.
        A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def sub_search(w, tree):
            for i in range(len(w)):
                if w[i] == '.':
                    for k, sub_tree in tree.iteritems():
                        if k == 'end':
                            continue
                        if sub_search(w[i+1:], sub_tree):
                            return True
                    return False
                else:
                    if w[i] not in tree:
                        return False
                    else:
                        tree = tree[w[i]]
            return 'end' in tree
        return sub_search(word, self.tree)

