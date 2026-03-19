class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
             return False

        word1chars = {}
        word2chars = {}

        for i in range(len(word1)):
            if word1[i] in word1chars:
                word1chars[word1[i]] += 1
            else:
                word1chars[word1[i]] = 1

        for i in range(len(word2)):
            if word2[i] in word2chars:
                word2chars[word2[i]] += 1
            else:
                word2chars[word2[i]] = 1
        
        return sorted(word1chars.keys()) == sorted(word2chars.keys()) and sorted(word1chars.values()) == sorted(word2chars.values())