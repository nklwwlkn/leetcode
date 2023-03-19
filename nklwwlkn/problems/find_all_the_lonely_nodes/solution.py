# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(root):
            if not root:
                return None
            
            if not root.left or not root.right:
                node = root.left or root.right
                if node:
                    res.append(node.val)
            
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        return res