class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        totalvalue = 0
        acc = 0
        for i in range(len(nums)):
            totalvalue += nums[i]
        for i in range(len(nums)):
            if acc*2 == (totalvalue - nums[i]):
                return i
            acc += nums[i]
        return -1