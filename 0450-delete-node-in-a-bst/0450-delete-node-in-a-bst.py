# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        node=root
        if node is None:
            return node
        if key> node.val:
            node.right=self.deleteNode(node.right,key)
        elif key < node.val:
            node.left=self.deleteNode(node.left,key)

        else:
            #we found the node we want to delete
            #single child case
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            #else thre will be two children
            #replace with max in left sub tree
            current=node.left
            while current.right:
                current=current.right
            node.val=current.val
            node.left=self.deleteNode(node.left,node.val)
        return node        