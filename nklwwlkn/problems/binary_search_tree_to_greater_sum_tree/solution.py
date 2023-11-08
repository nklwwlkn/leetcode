# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(root, prev):
            if not root:
                return prev

            prev = dfs(root.right, prev)
            prev += root.val
            root.val = prev
            prev = dfs(root.left, prev)

            return prev
        
        dfs(root, 0)

        return root
        
        