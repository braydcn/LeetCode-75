# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        result = None
        currentNode = root
        while not result and currentNode:
            if val > currentNode.val:
                currentNode = currentNode.right
            elif val < currentNode.val:
                currentNode = currentNode.left
            else:
                result = currentNode
        return result