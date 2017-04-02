# coding: utf8

class Solution(object):
    # 将递归优化成迭代，先计算在更新下标，重构能够解决好多分支条件
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 2:
            return 0
        lf = 0
        rt = len(height) - 1
        while (height[lf] == 0 and lf < rt):
            lf += 1
        while (height[rt] == 0 and lf < rt):
            rt -= 1
        if rt - lf <= 1:
            return 0
        lh = height[lf]
        rh = height[rt]
        def subP(lh, rh, lf, rt):
            if lf >= rt:
                if lh <= rh and lh > height[rt]:
                    return lh - height[rt]
                elif lh > rh and rh > height[lf]:
                    return rh - height[lf]
                else:
                    return 0
            if lh <= rh:
                if height[lf] >= lh:
                    lh = height[lf]
                    current = 0
                else:
                    current = lh - height[lf]
                return current + subP(lh, rh, lf+1, rt)
            else:
                if height[rt] >= rh:
                    rh = height[rt]
                    current = 0
                else:
                    current = rh - height[rt]
                return current + subP(lh, rh, lf, rt-1)
        return subP(lh, rh, lf+1, rt-1)

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lf = 0
        rt = len(height) - 1
        level = min(height[lf], height[rt])
        water = 0
        while rt > lf:
            if height[lf] < height[rt]:
                lower = height[lf]
                lf += 1
            else:
                lower = height[rt]
                rt -= 1
            if lower > level:
                level = lower
            water += level - lower
        return water


if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print Solution().trap(height)
