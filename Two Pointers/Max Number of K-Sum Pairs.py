class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Hash table way
        # combinations = 0
        # numbersseen = {}
        # for i in range(len(nums)):
        #     target = k - nums[i]
        #     if target in numbersseen and numbersseen[target] > 0:
        #         numbersseen[target] -= 1
        #         combinations += 1
        #     else:
        #         if nums[i] in numbersseen:
        #             numbersseen[nums[i]] += 1
        #         else:
        #             numbersseen[nums[i]] = 1
        # return combinations

        # 2 pointer way
        combinations = 0
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == k:
                combinations += 1
                right -= 1
                left += 1
            elif nums[left] + nums[right] > k:
                right -= 1
            else:
                left += 1
        return combinations
        