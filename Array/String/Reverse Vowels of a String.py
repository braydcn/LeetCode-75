class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # newstring = []
        # vowels = []
        # for i in range(len(s)):
        #     if s[i] in "AEIOUaeiou":
        #         vowels.append(s[i])
        # counter = 0
        # reversed_vowels = vowels[::-1]
        # for i in range(len(s)):
        #     if s[i] in "AEIOUaeiou":
        #         newstring.append(reversed_vowels[counter])
        #         counter += 1
        #     else:
        #         newstring.append(s[i])
        # return "".join(newstring)

        s = list(s)
        left = 0
        right = len(s) - 1
        vowels = set("AEIOUaeiou") # Set uses a hash table, so its quicker than string lookup
        while left < right:
            if s[left] in vowels and s[right] in vowels:
                # temp = s[left]
                # s[left] = s[right]
                # s[right] = temp
                s[left], s[right] = s[right], s[left] # quicker assignment than a temp
                right -= 1
                left += 1
            elif s[left] in vowels:
                right -= 1
            else:
                left += 1

        return "".join(s)