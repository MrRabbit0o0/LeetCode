# coding: utf8

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(cmp=lambda x, y: -1 if x[0] < y[0] or x[0] == y[0] and x[1] > y[1] else 1)
        def lmip(tails, k):
            b, e = 0, len(tails) - 1
            while b <= e:
                mid = (b + e) / 2
                if envelopes[tails[mid]][1] >= k[1]:
                    e = mid - 1
                else:
                    b = mid + 1
            return b

        tails = []
        for i, en in enumerate(envelopes):
            idx = lmip(tails, en)
            if idx > len(tails) - 1:
                tails.append(i)
            else:
                tails[idx] = i
        return len(tails)

if __name__ == '__main__':
    envelopes = [[5,4],[6,4],[6,7],[2,3]]
    print envelopes
    print Solution().maxEnvelopes(envelopes)

    envelopes = [[17,18],[20,4],[4,3],[14,6],[16,4],[8,11],[17,11],[18,7],[20,12]]
    print envelopes
    print Solution().maxEnvelopes(envelopes)

