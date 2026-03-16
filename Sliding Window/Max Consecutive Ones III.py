class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        zeroesfound = 0
        maxcons = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeroesfound += 1
            if zeroesfound > k:
                left += 1
                if nums[left-1] == 0:
                    zeroesfound -= 1
            if right - left + 1 > maxcons:
                maxcons = right - left + 1
        return maxcons