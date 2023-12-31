# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        res = defaultdict(list)

        level = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()

                if node:
                    res[level].append(node.val)

                    if node.left:
                        q.append(node.left)

                    if node.right:
                        q.append(node.right)
            level += 1
        
        return res.values()