# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        length=len(nums)

        def buildTree(nums, start,end):
            if start > end:
                return None
            current=nums[start]
            index=start
            for i in range(start,end+1):
                if nums[i] > current:
                    current=nums[i]
                    index=i
            current_node=TreeNode(current)
            if start==end:
                return current_node
            current_node.left=buildTree(nums,start,index-1)
            current_node.right=buildTree(nums,index+1,end)
            return current_node
        return buildTree(nums,0,length-1)

        