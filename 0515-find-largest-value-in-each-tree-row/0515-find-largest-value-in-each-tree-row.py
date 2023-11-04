# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        queue=[]
        queue.append(root)
        result=[]
        if root is None:
            return []
        while(queue):
            q_len=len(queue)
            maxval=float('-inf')
            for i in range(q_len):
                node=queue.pop(0)
                maxval=max(maxval,node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(maxval)
            
        return result
        