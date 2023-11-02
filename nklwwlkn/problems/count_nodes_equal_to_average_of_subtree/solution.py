# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        counter = [0]
        def dfs(root):
            if not root:
                return [0, 0]
            
            countLeft, sumLeft = dfs(root.left)
            countRight, sumRight = dfs(root.right)

            count = countLeft + countRight + 1
            summ = sumLeft + sumRight + root.val

            if summ // count == root.val:
                counter[0] += 1

            return [count, summ]
        
        dfs(root)

        return counter[0]