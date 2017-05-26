# coding: utf8

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if not preorder:
            return True
        if preorder[0] == '#':
            return len(preorder) == 1
        preorder = preorder.split(',')
        node_stack = []
        for i in range(len(preorder)):
            c = preorder[i]
            if c != '#':
                node_stack.append(2)
            else:
                try:
                    node_stack[-1] -= 1
                    while node_stack and node_stack[-1] == 0:
                        node_stack.pop(-1)
                        if not node_stack:
                            return i == len(preorder) - 1
                        node_stack[-1] -= 1
                except:
                    return False
        return False


if __name__ == '__main__':
    preorder = '9,3,4,#,#,1,#,#,2,#,6,#,#'
    print preorder
    print Solution().isValidSerialization(preorder)
    preorder = '9,#,#,1,#,#,2,#,6,#,#'
    print preorder
    print Solution().isValidSerialization(preorder)
    preorder = '1,#,#'
    print preorder
    print Solution().isValidSerialization(preorder)
