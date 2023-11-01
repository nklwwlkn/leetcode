# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        hm = dict()
        res = []

        def dfs(root):
            if not root:
                return None
            
            hm[root.val] = hm.get(root.val, 0) + 1 

            dfs(root.left)
            dfs(root.right)

            return root.val
        
        dfs(root)

        maxNodes = max(hm.values())
        
        for key, value in hm.items():
            if value == maxNodes:
                res.append(key)
        
        return res
            

        
        
        

        
        