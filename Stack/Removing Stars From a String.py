class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []

        for char in s:
            if char != "*":
                result.append(char)
            else:
                result.pop()
        return "".join(result)