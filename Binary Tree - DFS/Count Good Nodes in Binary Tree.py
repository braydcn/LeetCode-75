# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        validnodes = [0]
        def dfs(node, highestpathnode):
            if node is None:
                return   
            if node != root and node.val >= highestpathnode:
                highestpathnode = node.val
                validnodes[0] += 1
            dfs(node.left, highestpathnode)
            dfs(node.right, highestpathnode)
            return
        dfs(root, root.val)
        return validnodes[0] + 1