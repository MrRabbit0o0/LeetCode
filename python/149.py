# coding: utf8

# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        from fractions import gcd
        def compute_line(p1, p2):
            if p1.y == p2.y:
                return 'x-axis', p1.y
            elif p1.x == p2.x:
                return 'y-axis', p1.x
            else:
                y_ = p1.y - p2.y
                x_ = p1.x - p2.x
                d = gcd(y_, x_)
                a = y_ / d
                b = x_ / d
                c = p1.y - a * p1.x / b
                return a, b, c

        if len(points) <= 1:
            return len(points)
        line_dict = {}
        for i in range(len(points)-1):
            p1 = points[i]
            for j in range(i+1, len(points)):
                p2 = points[j]
                key = compute_line(p1, p2)
                if key not in line_dict:
                    line_dict[key] = set()
                line_dict[key].add(i)
                line_dict[key].add(j)

        return max(map(len, line_dict.itervalues()))

if __name__ == '__main__':
    points = []
    p = [(0, 0), (0, 0)]
    points.append(p)

    p = [(0, 4), (0, 3), (0, 2)]
    points.append(p)

    p = [(-5, 3), (3, 3), (2, 3)]
    points.append(p)

    p = [[560,248],[0,16],[30,250],[950,187],[630,277],[950,187],[-212,-268],[-287,-222],[53,37],[-280,-100],[-1,-14],[-5,4],[-35,-387],[-95,11],[-70,-13],[-700,-274],[-95,11],[-2,-33],[3,62],[-4,-47],[106,98],[-7,-65],[-8,-71],[-8,-147],[5,5],[-5,-90],[-420,-158],[-420,-158],[-350,-129],[-475,-53],[-4,-47],[-380,-37],[0,-24],[35,299],[-8,-71],[-2,-6],[8,25],[6,13],[-106,-146],[53,37],[-7,-128],[-5,-1],[-318,-390],[-15,-191],[-665,-85],[318,342],[7,138],[-570,-69],[-9,-4],[0,-9],[1,-7],[-51,23],[4,1],[-7,5],[-280,-100],[700,306],[0,-23],[-7,-4],[-246,-184],[350,161],[-424,-512],[35,299],[0,-24],[-140,-42],[-760,-101],[-9,-9],[140,74],[-285,-21],[-350,-129],[-6,9],[-630,-245],[700,306],[1,-17],[0,16],[-70,-13],[1,24],[-328,-260],[-34,26],[7,-5],[-371,-451],[-570,-69],[0,27],[-7,-65],[-9,-166],[-475,-53],[-68,20],[210,103],[700,306],[7,-6],[-3,-52],[-106,-146],[560,248],[10,6],[6,119],[0,2],[-41,6],[7,19],[30,250]]
    points.append(p)

    for p in points:
        print p
        ps = []
        for a, b in p:
            ps.append(Point(a, b))
        print Solution().maxPoints(ps)
