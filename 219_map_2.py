class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        store = set()
        for i, num in enumerate(nums):
            if num in store:
                return True
            store.add(num)
            if len(store) > k:
                store.remove(nums[i-k])

        return False
