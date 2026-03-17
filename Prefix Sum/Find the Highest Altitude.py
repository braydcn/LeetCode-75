class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        acc = 0
        maxalt = acc
        for i in range(len(gain)):
            acc += gain[i]
            if acc > maxalt:
                maxalt = acc
        return maxalt