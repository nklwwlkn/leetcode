# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([(0, root)])
        hm = defaultdict(list)

        while q:
            for _ in range(len(q)):
                vLevel, node = q.popleft()

                if node:
                    hm[vLevel].append(node.val)
                    if node.left:
                        q.append((vLevel - 1, node.left))
                    
                    if node.right:
                        q.append((vLevel + 1, node.right))

        return [value for key, value in sorted(hm.items())]

        

        