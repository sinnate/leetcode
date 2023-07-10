# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Just in case
        if root == None :
            return 0
        # If both the left and right are None retun height = 1
        if root.left == None and root.right == None :
            return 1
        
        # if either subtree is None, we will recur the other subtree 
        if root.left is None :
            return self.minDepth(root.right)+1
        elif root.right is None :
            return self.minDepth(root.left)+1
        return min(self.minDepth(root.left), self.minDepth(root.right))+1