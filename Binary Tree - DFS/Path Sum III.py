# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        occurences = [0]
        def dfs(node, currentsum):
            if node is None:
                return 0
            currentsum += node.val
            if currentsum == targetSum:
                count = 1
            else:
                count = 0
            count += dfs(node.left, currentsum)
            count += dfs(node.right, currentsum)
            return count

        def traverse(node):
            if node is None:
                return 0
            return dfs(node, 0) + traverse(node.left) + traverse(node.right)

        return traverse(root)
