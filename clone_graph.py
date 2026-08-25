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
        if not node: 
            return node

        stack = [node]
        o_to_n = {node:Node(node.val)}

        while stack: 
            curr = stack.pop()
            for neigh in curr.neighbors:
                if neigh not in o_to_n:
                    copy = Node(neigh.val)
                    o_to_n[neigh] = copy
                    stack.append(neigh)
                o_to_n[curr].neighbors.append(o_to_n[neigh])
        return o_to_n[node]
        