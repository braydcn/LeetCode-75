class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        longestsize = 0
        zeroescounted = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeroescounted += 1
            while zeroescounted > 1:
                if nums[left] == 0:
                    zeroescounted -= 1
                left += 1
            if right - left > longestsize:
                longestsize = right - left
        return longestsize