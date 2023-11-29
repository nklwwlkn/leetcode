"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        originalToCopy = dict()

        def clone(root):
            if not root:
                return None

            if root in originalToCopy:
                return originalToCopy[root]

            copy = Node(root.val)
            originalToCopy[root] = copy

            for child in root.children:
                copy.children.append(clone(child))

            return copy
        
        return clone(root) if root else None