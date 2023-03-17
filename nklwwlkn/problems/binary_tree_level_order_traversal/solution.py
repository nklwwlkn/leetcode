# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        level = 0
        d = defaultdict(list)

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                if node:
                    d[level].append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            level += 1
        
        return d.values()