# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        if root is None:
            return
        #add root to result
        if not self.isLeaf(root):
            result.append(root.val)

        self.leftBoundary(root,result)
        self.addLeaves(root,result)
        self.rightBoundaryreverse(root,result)
        return result

    def isLeaf(self,root):
        if root.left is None and root.right is None:
            return True
        return False

    def addLeaves(self,root,result):
        if root is None:
            return
        if self.isLeaf(root):
            result.append(root.val)
        self.addLeaves(root.left,result)
        self.addLeaves(root.right,result)
    
    def leftBoundary(self,root,result):
        root=root.left
        while root:
            if not self.isLeaf(root):
                result.append(root.val)
            if root.left is not None:
                root=root.left
            else:
                root=root.right
    def rightBoundaryreverse(self,root,result):
        right=[]
        root=root.right
        while root:
            if not self.isLeaf(root):
                right.append(root.val)
            if root.right is not None:
                root=root.right
            else:
                root=root.left
        for i in range(len(right)):
            result.append(right.pop(-1))
        