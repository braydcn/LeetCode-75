class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        highestcandy = 0
        booleantable = []
        for i in range(len(candies)):
            if candies[i] > highestcandy:
                highestcandy = candies[i]
        for i in range(len(candies)):
            booleantable.append(candies[i] + extraCandies >= highestcandy)
        return booleantable