# coding: utf8

class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        max_length = 0
        dir_stack = []
        input = input + '\n'
        i = 0
        while i < len(input):
            dir_depth = 0
            while input[i] == '\t':
                dir_depth += 1
                i += 1
            file_name = ''
            is_file = False
            while input[i] != '\n':
                file_name += input[i]
                i += 1
                if input[i] == '.':
                    is_file = True
            if input[i] == '\n':
                if is_file:
                    dir_stack = dir_stack[:dir_depth]
                    length = len('/'.join(dir_stack[:dir_depth] + [file_name]))
                    max_length = max(max_length, length)
                else:
                    dir_stack = dir_stack[:dir_depth] + [file_name]
                    dir_depth += 1
            i += 1
        return max_length


if __name__ == '__main__':
    input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    print Solution().lengthLongestPath(input)
    input = "dir\n        file1.ext"
    print Solution().lengthLongestPath(input)

