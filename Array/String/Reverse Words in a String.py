class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # words = []
        # currentwordadding = ""
        # for i in range(len(s)):
        #     if s[i] == " ":
        #         if currentwordadding != "":
        #             words.append(currentwordadding)
        #             currentwordadding = ""
        #     else:
        #         currentwordadding += s[i]
        # if currentwordadding:
        #     words.append(currentwordadding)
        # words.reverse()
        # return " ".join(words)

        return " ".join(reversed(s.split()))