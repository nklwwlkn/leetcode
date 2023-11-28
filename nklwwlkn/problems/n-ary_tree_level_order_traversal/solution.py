"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        levelByVal = defaultdict(list)
        q = deque([root])

        level = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()

                if node:
                    
                    levelByVal[level].append(node.val)

                    for child in node.children:
                        q.append(child)
            
            level += 1
        

        return levelByVal.values()
                
        