class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        current = 0
        for i in range(k):
            if s[i] in "aeiou":
                current += 1
        maxnum = current

        for i in range(k, len(s)):
            if s[i - k] in "aeiou":
                current -=1
            if s[i] in "aeiou":
                current += 1
            if current > maxnum:
                maxnum = current
        return maxnum