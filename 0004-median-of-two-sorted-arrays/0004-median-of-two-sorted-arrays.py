import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []
        median = 0
        for i in nums1:
            nums3.append(i)
        for j in nums2:
            nums3.append(j)
        nums3.sort()
        print(nums3)
        y = math.floor(len(nums3)/2)
        x = len(nums3)
        if x%2 ==0:
            x = x/2
            z = (nums3[y]+ nums3[y-1])/2
            return z
        return nums3[y]