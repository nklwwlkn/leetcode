# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int, res = []) -> List[List[int]]:
        res = []

        def dfs(root, currentSum = 0, currentPath = []):
            if not root:
                return None
            
            currentPath.append(root.val)
            currentSum += root.val

            if not root.left and not root.right and currentSum == targetSum:
                res.append(currentPath[:])
            
            dfs(root.left, currentSum, currentPath)
            dfs(root.right, currentSum, currentPath)

            currentPath.pop()

        dfs(root)

        return res

        