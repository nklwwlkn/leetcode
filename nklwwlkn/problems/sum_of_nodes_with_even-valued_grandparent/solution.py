# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = [0]
        def dfs(root, parent = -1, grandParent = -1):
            if not root:
                return 0

            res[0] += root.val if grandParent % 2 == 0 else 0
            
            dfs(root.left, root.val, parent)
            dfs(root.right, root.val, parent)
        
        dfs(root)

        return res[0]