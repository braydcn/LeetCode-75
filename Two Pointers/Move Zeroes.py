class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        write = 0

        for read in range(len(nums)):
            if nums[read] != 0:
                temp = nums[write]
                nums[write] = nums[read]
                nums[read] = temp
                write += 1
        return nums
