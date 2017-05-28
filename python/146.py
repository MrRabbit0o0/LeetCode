# coding: utf8

class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.key_value = {}
        self.length = 0
        self.track_head = Node(-1, -1)
        self.track_tail = Node(-1, -1)
        self.track_head.next = self.track_tail
        self.track_tail.prev = self.track_head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.key_value:
            node = self.key_value[key]
            self.update(node)
            return node.val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.key_value:
            node = self.key_value[key]
            node.val = value
            self.update(node)
            return
        if self.length == self.capacity:
            del_key = self.track_head.next.key
            del self.key_value[del_key]
            self._remove(self.track_head.next)
        else:
            self.length += 1

        node = Node(key, value)
        self.key_value[key] = node
        self._add(node)

    def update(self, node):
        self._remove(node)
        self._add(node)

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add(self, node):
        node.prev = self.track_tail.prev
        node.prev.next = node
        node.next = self.track_tail
        node.next.prev = node
