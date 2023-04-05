# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque([[root, float('-inf')]])
        counter = 0

        while q:
            for _ in range(len(q)):
                node, maxValue = q.popleft()

                if node:
                    if node.val >= maxValue:
                        maxValue = node.val
                        counter += 1
                    
                    q.append([node.left, maxValue])
                    q.append([node.right, maxValue])

        
        return counter
        