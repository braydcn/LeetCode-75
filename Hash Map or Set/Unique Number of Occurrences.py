class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        hashmap = {}
        hash2 = {}

        for i in range(len(arr)):
            if arr[i] in hashmap:
                hashmap[arr[i]] += 1
            else:
                hashmap[arr[i]] = 1

        for i in hashmap.values():
            if i in hash2:
                return False
            else:
                hash2[i] = True
        return True