# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)

        def dfs(root, counter = 0):
            if not root:
                return 0
        
            left = dfs(root.left, counter)
            right = dfs(root.right, counter)

            counter = max(left, right)

            res[counter].append(root.val)
            
            return counter + 1

        dfs(root)


        return res.values()

        