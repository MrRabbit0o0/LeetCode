# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sums = None
        while (l1 is not None) and (l2 is not None):
            if sums is None:
                sums = ListNode(0)
                original = sums
            else:
                sums = sums.next

            num = l1.val + l2.val+sums.val
            if num >= 10:
                sums.val = num-10
                sums.next = ListNode(1)
            else:
                sums.val = num
                sums.next = ListNode(0)
            l1 = l1.next
            l2 = l2.next

        if l1 is not None:
            self.__remainder(l1, sums)
        elif l2 is not None:
            self.__remainder(l2, sums)
        elif sums.next.val is 0:
            sums.next = None
        return original

    def __remainder(self, remainder, sums):
        sums = sums.next
        while remainder is not None:
            num = remainder.val + sums.val
            if num < 10:
                sums.val = num
                sums.next = remainder.next
                break
            else:
                sums.val = num-10
                sums.next = ListNode(1)
                sums = sums.next
                remainder = remainder.next


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

s = Solution()

l1 = ListNode(3)
l1.next = ListNode(7)

l2 = ListNode(9)
l2.next = ListNode(2)

print s.addTwoNumbers(l1, l2).val
