class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n < 3:
            return 0

        slow = -1
        visited = [-1 for _ in range(26)]
        quick = 0
        cnt = 0
        while quick < n:
            c = s[quick]
            pos = ord(c) - ord('a')
            if visited[pos] != -1:
                slow = max(slow, visited[pos])

            visited[pos] = quick
            if quick - slow >= 3:
                cnt += 1

            quick += 1

        return cnt
