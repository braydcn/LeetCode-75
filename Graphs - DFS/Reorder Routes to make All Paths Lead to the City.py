from collections import defaultdict

class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))

        visited = set([0])
        changes = [0]

        def dfs(node):
            for neighbor, cost in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    changes[0] += cost
                    dfs(neighbor)
        dfs(0)
        return changes[0]