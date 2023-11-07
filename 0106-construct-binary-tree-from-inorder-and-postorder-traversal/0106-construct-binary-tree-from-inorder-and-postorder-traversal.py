# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        in_map={}
        #store indices of inorder
        for i in range(len(inorder)):
            in_map[inorder[i]]=i
        post_index=len(postorder)-1
        def tree(inorder,postorder, instart, inend):
            nonlocal post_index
            if instart>inend:
                return None           
            current=postorder[post_index]
            curr_node=TreeNode(current)
            post_index-=1
            in_index=in_map[current]
            if instart==inend:
                return curr_node
            curr_node.right=tree(inorder,postorder,in_index+1,inend)
            curr_node.left=tree(inorder,postorder,instart,in_index-1)
            return curr_node
        return tree(inorder,postorder,0,len(inorder)-1)
        