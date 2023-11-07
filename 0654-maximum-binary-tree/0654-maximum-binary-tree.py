# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        length = len(nums)

        def buildTree(start, end):
            if start > end:
                return None

            # Find the index of the maximum element within the current subrange
            max_index = start
            for i in range(start, end + 1):
                if nums[i] > nums[max_index]:
                    max_index = i

            current_node = TreeNode(nums[max_index])

            current_node.left = buildTree(start, max_index - 1)
            current_node.right = buildTree(max_index + 1, end)
            return current_node

        return buildTree(0, length - 1)

        