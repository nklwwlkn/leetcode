# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, prevMin = - math.inf, prevMax = math.inf):
            if not root:
                return True
            
            if not prevMin < root.val < prevMax:
                return False
            
            return dfs(root.left, prevMin, root.val) and dfs(root.right, root.val, prevMax)
        
        return dfs(root)