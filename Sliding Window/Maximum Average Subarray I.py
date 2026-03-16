class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        current = sum(nums[:k])
        maxnum = current

        for i in range(k, len(nums)):
            current +=  nums[i] - nums[i - k]
            if current > maxnum:
                maxnum = current
        return maxnum/float(k)