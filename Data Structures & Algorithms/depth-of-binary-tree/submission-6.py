# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        maxLvl = 1
        self.dfs(root)

        
    def dfs(self, root):
        if root.left or root.right:
            maxLvl += 1
        dfs(root.left)
        dfs(root.right)
        
        