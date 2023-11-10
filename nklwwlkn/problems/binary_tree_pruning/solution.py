# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return True

            leftSubtree = dfs(root.left)
            rightSubtree = dfs(root.right)

            if leftSubtree:
                root.left = None
            if rightSubtree:
                root.right = None

            return root.val == 0 and leftSubtree and rightSubtree

        dfs(root)

        return None if dfs(root) else root

    