class Solution(object):
    def mergeAlternately(self, word1, word2):
        combined = [] # use list instead of string since youre creating new strings when you do combined + combined
        lastindex = 0
        for i in range(min(len(word1), len(word2))):
            combined.append(word1[i])
            combined.append(word2[i])
            lastindex = i
        combined.append(word1[lastindex+1:])
        combined.append(word2[lastindex+1:])
        return "".join(combined)