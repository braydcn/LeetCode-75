class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        hashmap = {}
        for i in range(len(grid)):
            if tuple(grid[i]) in hashmap:
                hashmap[tuple(grid[i])] += 1
            else:
                hashmap[tuple(grid[i])] = 1

        for i in range(len(grid)):
            column = []
            for j in range(len(grid)):
                column.append(grid[j][i])
            if tuple(column) in hashmap:
                result += hashmap[tuple(column)]
        return result