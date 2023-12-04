"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeToCopy = dict()

        def clone(node):
            if node in nodeToCopy:
                return nodeToCopy[node]
            
            copy = Node(node.val)
            nodeToCopy[node] = copy

            for n in node.neighbors:
                nodeToCopy[node].neighbors.append(clone(n))

            return copy 


        return clone(node) if node else None
        