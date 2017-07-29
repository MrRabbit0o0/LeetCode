# coding: utf8

class RandomizedCollection(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val_list = []
        self.random_map = collections.defaultdict(set)

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.random_map[val].add(len(self.val_list))
        self.val_list.append(val)
        return len(self.random_map[val]) == 1

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if self.random_map[val]:
            idx = self.random_map[val].pop()
            new_val = self.val_list[-1]
            if idx != len(self.val_list) - 1:
                self.val_list[idx] = new_val
                self.random_map[new_val].discard(len(self.val_list)-1)
                self.random_map[new_val].add(idx)
                self.val_list.pop(-1)
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.val_list)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
