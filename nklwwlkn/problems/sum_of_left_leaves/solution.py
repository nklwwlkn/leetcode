# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(root, parent = None):
            if not root:
                return 0

            left = dfs(root.left, root)
            res[0] += root.val if not root.left and not root.right and parent and root == parent.left else 0
            right = dfs(root.right, root)

            return 0

        dfs(root)

        return res[0]
        