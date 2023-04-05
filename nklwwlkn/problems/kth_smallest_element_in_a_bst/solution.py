# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = [0]
        res = [0]
        def dfs(root):
            if not root:
                return 0

            dfs(root.left)
            counter[0] += 1
            if counter[0] == k:
                res[0] = root.val
            dfs(root.right)
        
        dfs(root)
        
        return res[0]

        
                
            
        