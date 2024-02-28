# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        tree_map={}
        queue=[]
        queue.append(root)

        y_cord=0
        while(queue):
            q_len=len(queue)
            
            for i in range(q_len):
                node=queue.pop(0)
                if y_cord not in tree_map:
                    tree_map[y_cord]  = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            y_cord=y_cord+1
        return tree_map[y_cord-1]

        