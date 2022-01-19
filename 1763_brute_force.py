class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        max_len = 0
        ii = 0
        jj = 0

        for i in range(n):
            for j in range(i+1, n+1):
                if j - i < 2:
                    continue
                if j - i <= max_len:
                    continue
                if self.is_nice(s[i:j]):
                    max_len = j - i
                    ii = i
                    jj = j

        if max_len == 0:
            return ''

        return s[ii:jj]

    def is_nice(self, s):
        store = set()
        for c in s:
            store.add(c)
        for c in s:
            if c.islower() and c.upper() not in store:
                return False
            if c.isupper() and c.lower() not in store:
                return False
        return True
