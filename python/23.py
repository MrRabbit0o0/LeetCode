# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ret = ListNode(None)
        lists = filter(None, lists)
        if lists:
            self.__mergeKlists(lists, ret)
        return ret.next

    def __mergeKlists(self, lists, pointer):
        while len(filter(None, lists)) > 1:
            min_node_index = self.__min_node_index(lists)
            min_node = lists[min_node_index]
            pointer.next = min_node
            pointer = pointer.next
            lists[min_node_index] = min_node.next
            lists = filter(None, lists)
        if lists:
            pointer.next = lists[0]

    def __min_node_index(self, lists):
        min_value = lists[0].val
        min_index = 0
        for index, node in enumerate(lists):
            if node.val < min_value:
                min_value = node.val
                min_index = index
        return min_index


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


s = Solution()
ret = s.mergeKLists([None])
while ret:
    print ret.val
    ret = ret.next
