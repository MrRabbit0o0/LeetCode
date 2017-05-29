# coding: utf8

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1l = version1.split('.', 1) + ['0']
        v2l = version2.split('.', 1) + ['0']
        v1, ver1 = int(v1l[0]), v1l[1]
        v2, ver2 = int(v2l[0]), v2l[1]

        if v1 > v2:
            return 1
        elif v1 < v2:
            return -1
        else:
            return self.compareVersion(ver1, ver2) if ver1 != ver2 else 0


if __name__ == '__main__':
    version1 = '1'
    version2 = '1.3'
    print version1, version2
    print Solution().compareVersion(version1, version2)
