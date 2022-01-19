class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n < 3:
            return 0

        store = {}
        cnt = 0
        i = 0
        while i < n:
            if i < 2:
                store.setdefault(s[i], 0)
                store[s[i]] += 1
                i += 1
                continue

            if i > 2:
                c_to_remove = s[i-3]
                if store[c_to_remove] == 1:
                    store.pop(c_to_remove)
                else:
                    store[c_to_remove] -= 1

            store.setdefault(s[i], 0)
            store[s[i]] += 1
            if len(store) == 3:
                cnt += 1

            i += 1

        return cnt
