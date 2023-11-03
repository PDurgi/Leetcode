# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=[]
        level_nodes = collections.defaultdict(list)
        queue= collections.deque([(0,root)])
        x_min=float('inf')
        x_max=float('-inf')
        if not root:
            return []
        while queue:
            x_cord,node=queue.popleft()
            level_nodes[x_cord].append(node.val)
            x_min=min(x_min,x_cord)
            x_max=max(x_max,x_cord)
            if node.left:
                queue.append([x_cord-1,node.left])
            if node.right:
                queue.append([x_cord+1,node.right])
        for i in range(x_min,x_max+1):
            result.append(level_nodes[i])
        return result


        
        