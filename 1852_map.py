class Solution(object):
    def distinctNumbers(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        s = {}
        n = len(nums)
        ans = []
        if n < k:
            return ans

        for i in range(k):
            if nums[i] in s:
                s[nums[i]] += 1
            else:
                s[nums[i]] = 1
        ans.append(len(s))

        for i in range(k, n):
            if s[nums[i-k]] == 1:
                s.pop(nums[i-k])
            else:
                s[nums[i-k]] -= 1

            if nums[i] in s:
                s[nums[i]] += 1
            else:
                s[nums[i]] = 1

            ans.append(len(s))

        return ans
