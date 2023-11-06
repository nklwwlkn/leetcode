# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        counter = 0
        q = deque([[root, float("-inf")]])

        while q:
            for _ in range(len(q)):
                node, maxValue = q.popleft()

                if node:
                    if node.val >= maxValue:
                        counter += 1
                        maxValue = node.val
                    q.append([node.left, maxValue])
                    q.append([node.right, maxValue])
        
        return counter
