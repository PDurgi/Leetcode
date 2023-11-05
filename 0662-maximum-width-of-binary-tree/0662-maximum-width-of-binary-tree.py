# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #bfs lofic plus track indices
        #root,index,level
        queue=collections.deque([(root,1,0)])
        result=0
        prevlevel=0
        previndex=1
        while queue:
            node,index,level=queue.popleft()
            #to keep track of first index in each level
            if level>prevlevel:
                prevlevel=level
                previndex=index
            result=max(result, index-previndex+1)
            if node.left:
                queue.append([node.left, 2* index , level+1])
            if node.right:
                queue.append([node.right ,2*index +1 , level+1])
        return result

