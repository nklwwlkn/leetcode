# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root, prev = 0):
            if not root:
                return prev
            
            prev = dfs(root.right, prev)
            prev += root.val
            root.val = prev
            prev = dfs(root.left, prev)

            return prev

        dfs(root)    
    
        return root
        