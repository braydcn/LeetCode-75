from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        queue = deque([root])
        smallestLevel = 0
        currentLevel = 0
        bestSum = float('-inf')

        while queue:
            levelSize = len(queue)
            levelSum = 0
            currentLevel += 1
        
            for i in range(levelSize):
                node = queue.popleft()
            
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
                levelSum += node.val
            if levelSum > bestSum:
                bestSum = levelSum
                smallestLevel = currentLevel
        return smallestLevel