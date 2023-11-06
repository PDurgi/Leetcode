from collections import defaultdict, deque
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=[]
        level_nodes = collections.defaultdict(dict)
        queue= collections.deque([(0,root)])
        x_min=float('inf')
        x_max=float('-inf')
        y_cord=0
        y_min=0
        y_max=0
        if not root:
            return []
        while queue:
            q_len=len(queue)
            for i in range(len(queue)):
                x_cord,node=queue.popleft()
                if y_max not in level_nodes[x_cord]:
                    level_nodes[x_cord][y_max] = []
                level_nodes[x_cord][y_cord].append(node.val)
                x_min=min(x_min,x_cord)
                x_max=max(x_max,x_cord)
                if node.left:
                    queue.append((x_cord - 1, node.left))
                if node.right:
                    queue.append((x_cord + 1, node.right))

            y_cord+=1
            y_max+=1
        for i in range(x_min, x_max + 1):
            if i in level_nodes:
                level_values = []
                for j in range(y_min, y_max + 1):
                    if j in level_nodes[i]:
                        level_values.extend(sorted(level_nodes[i][j]))
                result.append(level_values)

        return result