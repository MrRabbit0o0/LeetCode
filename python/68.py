# coding: utf8

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if not words:
            return []
        text = []
        line_length = 0
        line = []
        for w in words:
            wl = len(w)
            if line_length == 0:
                new_length = wl
            else:
                new_length = line_length + wl + 1
            if new_length <= maxWidth:
                line.append(w)
                line_length = new_length
            else:
                text.append(line)
                line = [w]
                line_length = len(w)
        text.append(line)
        result = []
        for line in text[:-1]:
            space = maxWidth - sum([len(w) for w in line])
            if len(line) == 1:
                result.append(line[0] + ' ' * space)
                continue
            space_length = space / (len(line) - 1)
            new_line = (' ' * space_length).join(line)
            res = maxWidth - len(new_line)
            i = 0
            length = len(new_line)
            while i < length and res > 0:
                if new_line[i] == ' ':
                    new_line = new_line[:i] + ' ' + new_line[i:]
                    length += 1
                    i += 1
                    res -= 1
                i += 1
            result.append(new_line)
        line = text[-1]
        space = ' ' * (maxWidth - sum([len(w) + 1 for w in line]) + 1)
        result.append(' '.join(line) + space)
        return result

if __name__ == '__main__':
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    print words
    print maxWidth
    print
    for line in Solution().fullJustify(words, maxWidth):
        print line

    words = ["What","must","be","shall","be."]
    maxWidth = 12
    print words
    print maxWidth
    print
    for line in Solution().fullJustify(words, maxWidth):
        print line
    words = ["Don't","go","around","saying","the","world","owes","you","a","living;","the","world","owes","you","nothing;","it","was","here","first."]
    maxWidth = 30
    print words
    print maxWidth
    print
    for line in Solution().fullJustify(words, maxWidth):
        print line
