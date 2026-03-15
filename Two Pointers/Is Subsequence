class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        startposition = 0
        for target in range(len(s)):
            for i in range(startposition, len(t)):
                if s[target] == t[i]:
                    startposition = i + 1
                    break
            else:
                return False
        return True