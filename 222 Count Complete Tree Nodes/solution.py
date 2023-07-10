# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Just in case
        if root == None :
            return 0
        # If both the left and right are None retun height = 1
        if root.left == None and root.right == None :
            return 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
