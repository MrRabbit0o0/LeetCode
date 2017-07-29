# coding: utf8

class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        A = min([l[0] for l in rectangles])
        B = min([l[1] for l in rectangles])
        C = max([l[2] for l in rectangles])
        D = max([l[3] for l in rectangles])
        total = 0
        corner = {}
        def record(x):
            corner[x] = corner.get(x, 0) + 1
        for rec in rectangles:
            a, b, c, d = rec
            map(record, [(a, b), (a, d), (c, b), (c, d)])
            total += (c-a) * (d-b)
        if total != (C-A) * (D-B):
            return False

        for x in [(A, B), (A, D), (C, B), (C, D)]:
            if corner.get(x, 0) != 1:
                return False
            else:
                del corner[x]

        for val in corner.itervalues():
            if val % 2 == 1:
                return False
        return True





if __name__ == '__main__':
    rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
    print rectangles
    print Solution().isRectangleCover(rectangles)
