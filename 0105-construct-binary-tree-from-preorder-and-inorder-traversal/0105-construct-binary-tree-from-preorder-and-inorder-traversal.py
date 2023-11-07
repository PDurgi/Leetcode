# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        in_map={}
        #store indices of inorder
        for i in range(len(inorder)):
            in_map[inorder[i]]=i
        pre_index=0
        def tree(inorder,preorder, instart, inend):
            nonlocal pre_index
            if instart>inend:
                return None           
            current=preorder[pre_index]
            curr_node=TreeNode(current)
            pre_index+=1
            in_index=in_map[current]
            if instart==inend:
                return curr_node
            curr_node.left=tree(inorder,preorder,instart,in_index-1)
            curr_node.right=tree(inorder,preorder,in_index+1,inend)
            return curr_node
        return tree(inorder,preorder,0,len(inorder)-1)
        