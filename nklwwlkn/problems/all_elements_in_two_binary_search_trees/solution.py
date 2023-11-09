# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l1 = deque()
        l2 = deque()
        res = []

        def dfs(root, l):
            if not root: return

            dfs(root.left, l)
            l.append(root.val)
            dfs(root.right, l)
            
        
        dfs(root1, l1)
        dfs(root2, l2)

        while l1 and l2:
            if l1[0] < l2[0]:
                res.append(l1.popleft())
            else:
                res.append(l2.popleft())
        
        while l1:
            res.append(l1.popleft())

        while l2:
            res.append(l2.popleft())
       
        return res
        