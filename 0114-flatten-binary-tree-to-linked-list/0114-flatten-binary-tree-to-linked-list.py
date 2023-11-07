# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # the preorder of the tree has to be linkedlist
        # we have to rearrange nodes in place

        prev=None
        def linkedlist(root):
            nonlocal prev
            if root is None:
                return
            linkedlist(root.right)
            linkedlist(root.left)

            root.right=prev
            root.left=None
            prev=root
        return linkedlist(root)
    
        