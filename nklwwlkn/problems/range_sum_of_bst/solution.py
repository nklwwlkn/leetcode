# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = []
        def dfs(root, low, high):
            if not root:
                return None

            if low <= root.val <= high:
                res.append(root.val)
            left = dfs(root.left, low, high)
            right = dfs(root.right, low, high)
                

        dfs(root, low, high)

        return sum(res)