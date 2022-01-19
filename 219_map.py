class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        store = dict()
        for i, num in enumerate(nums):
            if num in store and i - store[num] <= k:
                return True
            store[num] = i

        return False
