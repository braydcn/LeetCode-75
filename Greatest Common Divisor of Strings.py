from fractions import gcd

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        gcdnumber = gcd(len(str1), len(str2))
        gcdtext = str1[:gcdnumber]
        if str1 + str2 == str2 + str1 : # both strings should be same added either way if they have a gcd of text
            return gcdtext
        else:
            return ""
