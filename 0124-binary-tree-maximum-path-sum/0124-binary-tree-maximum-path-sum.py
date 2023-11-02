# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # find the max left sum and right sum

        value = -1000
        def dfs(root):
            nonlocal value
            if root is None:
                return 0
            leftsum=max(0,dfs(root.left))
            rightsum=max(0,dfs(root.right))
            value=max(value,leftsum+rightsum+root.val)
            return root.val+max(leftsum,rightsum)
        
        dfs(root)
        return value
        