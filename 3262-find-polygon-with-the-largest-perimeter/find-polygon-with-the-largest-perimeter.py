class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        #bruteforce-> greedy
        #sort the array,
        nums.sort()
        size=len(nums)
        res=sum(nums)
        count=len(nums)
        perimeter=0
        for i in range(size-1,-1,-1):
            if res-nums[i]>nums[i]:
                return sum(nums)
            else:
                res=res-nums[i]
                nums.pop()                
                count=count-1
        if count<3:
            return -1
        return sum(nums)




                
