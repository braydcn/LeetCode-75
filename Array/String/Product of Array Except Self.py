class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [1] * len(nums)
        left = 1
        right = 1
        for i in range(1, len(nums)): # Left Loop, start at 1 since nothing to left of first
            left *= nums[i-1]
            answer[i] *= left
        for i in range(len(nums) - 2, -1, -1): # Right Loop, start at -2 of length since nothing to right of last
            right *= nums[i+1]
            answer[i] *= right
        return answer