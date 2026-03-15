class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        most = 0
        left = 0
        right = len(height) - 1

        while left < right:
            unitsbetween = right - left
            maxheight = min(height[left], height[right])
            if unitsbetween*maxheight > most:
                most = unitsbetween*maxheight
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return most