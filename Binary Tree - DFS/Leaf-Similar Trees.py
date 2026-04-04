# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        leaves1 = []
        leaves2 = []
    
        def dfs(node, leaves):
            if node is None:
                return
            if node.right == None and node.left == None:
                leaves.append(node.val)
            dfs(node.left, leaves)
            dfs(node.right, leaves)
    
        dfs(root1, leaves1)
        dfs(root2, leaves2)
        return leaves1 == leaves2