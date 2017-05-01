# coding: utf8

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area = (G - E) * (H -F) + (C - A) * (D - B)
        if E < C <= G or A < G <= C:
            if F < D <= H or B < H <= D:
                x1, x2 = sorted([A, C, E, G])[1:3]
                y1, y2 = sorted([B, D, F, H])[1:3]
                overlap = (y2 - y1) * (x2 - x1)
                area -= overlap
        return area
