class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        for i in range(n):
            for j in range(max(i-k, 0), i):
                if nums[i] == nums[j]:
                    return True
        return False
