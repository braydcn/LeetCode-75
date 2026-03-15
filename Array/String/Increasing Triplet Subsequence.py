class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        front = middle = float('inf')
        for num in nums:
            if num > middle:
                return True
            if num <= front:
                front = num
            else:
                middle = num
        return False