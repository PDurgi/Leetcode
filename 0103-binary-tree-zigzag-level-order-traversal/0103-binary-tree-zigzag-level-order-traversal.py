# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue=[]
        result=[]
        queue.append(root)
        reverseflag=0
        while queue:
            level=[]
            q_len=len(queue)
            for i in range(q_len):
                node=queue.pop(0)
                level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                
            if reverseflag==1:
                result.append(level[::-1])
                reverseflag=0
            else:
                result.append(level)
                reverseflag=1
        return result
        