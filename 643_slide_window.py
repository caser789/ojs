class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        if n < k:
            return 0.0

        _sum = 0
        for i in range(k-1):
            _sum += nums[i]

        _max_sum = -float('inf')
        for i in range(k-1, len(nums)):
            _sum += nums[i]
            if i-k>=0:
                _sum -= nums[i-k]

            if _sum > _max_sum:
                _max_sum = _sum

        return 1.0*_max_sum/k
