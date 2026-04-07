# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maxlength = 0

        def zigzag(node, came_from_left, length):
            if node is None:
                return
            self.maxlength = max(self.maxlength, length)
            if came_from_left:
                zigzag(node.right, False, length + 1)
                zigzag(node.left, True, 1)
            else:
                zigzag(node.left, True, length + 1)
                zigzag(node.right, False, 1)

        zigzag(root.left, True, 1)
        zigzag(root.right, False, 1)

        return self.maxlength