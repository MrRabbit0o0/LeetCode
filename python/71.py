# coding: utf8

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_list = filter(lambda x: x, path.split('/'))
        simple_path = []
        for x in path_list:
            if x == '.':
                continue
            elif x == '..':
                simple_path = simple_path[:-1]
            else:
                simple_path.append(x)
        return '/' + '/'.join(simple_path)


if __name__ == '__main__':
    path = '/d/a/c/./../e/'
    print path
    print Solution().simplifyPath(path)
    path = '////'
    print path
    print Solution().simplifyPath(path)
