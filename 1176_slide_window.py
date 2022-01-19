class Solution(object):
    def dietPlanPerformance(self, calories, k, lower, upper):
        """
        :type calories: List[int]
        :type k: int
        :type lower: int
        :type upper: int
        :rtype: int
        """
        n = len(calories)
        _sum = 0
        res = 0
        i = 0
        while i < n:
            _sum += calories[i]
            if i - k >= 0:
                _sum -= calories[i-k]

            if i + 1 - k >= 0:
                if _sum < lower:
                    res += -1
                if _sum > upper:
                    res += 1

            i += 1

        return res
