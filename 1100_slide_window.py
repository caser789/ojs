class Solution(object):
    def numKLenSubstrNoRepeats(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        counter = {}
        n = len(s)
        cnt = 0

        for i in range(k-1):
            c = s[i]
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1

        for i in range(k-1, n):
            if i-k >= 0:
                if counter[s[i-k]] == 1:
                    counter.pop(s[i-k])
                else:
                    counter[s[i-k]] -= 1

            c = s[i]
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1

            if len(counter) == k:
                cnt += 1

        return cnt
