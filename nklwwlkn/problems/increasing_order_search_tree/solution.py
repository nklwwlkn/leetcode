# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        res = []

        def dfs(root):
            if not root:
                return None
            
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        
        dfs(root)

        dummy = TreeNode()
        curr = dummy
        for num in res:
            curr.right = TreeNode(num)
            curr = curr.right
        
        return dummy.right
            