class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        n = len(arr)
        if n < k:
            return 0

        _sum = 0
        for i in range(k-1):
            _sum += arr[i]

        cnt = 0
        for i in range(k-1, n):
            _sum += arr[i]
            if i-k>=0:
                _sum -= arr[i-k]

            if _sum >= k * threshold:
                cnt += 1
        return cnt
