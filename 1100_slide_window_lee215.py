class Solution(object):
    def numKLenSubstrNoRepeats(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        cnt = 0
        i = 0
        store = set()
        for j in range(len(s)):
            while s[j] in store:
                store.remove(s[i])
                i += 1

            store.add(s[j])

            cnt += j-i+1 >= k

        return cnt
