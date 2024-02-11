from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
# recursive solution  -> basic       
        # size = len(nums)
        
        # def rob_t(size, nums):
        #     if size <= 0:
        #         return nums[size] if size == 0 else 0
        #     pick = nums[size] + rob_t(size - 2, nums)
        #     not_pick = rob_t(size - 1, nums)
        #     return max(pick, not_pick)
        
        # return rob_t(size-1, nums)
# memoization is similar-> we will maintain dp array and pass it in recursive calls. it is top down n->1

#dp tabulation approach -> bottom up -> 0 to n 
        size = len(nums)
        dp = [-1]*size
        dp[0]=nums[0]
        for i in range(1,len(nums)):
            pick = nums[i] 
            if i> 1:
                pick+= dp[i - 2]
            not_pick = dp[i - 1]
            dp[i]= max(pick, not_pick)        
        return dp[-1]

#dynamic programming space optimization on tabular approach
        # prev=nums[0]
        # prev2=0
        # current=0
        # for i in range(1,len(nums)):
        #     pick=nums[i]
        #     if i>1:
        #         pick=pick+prev2
        #     notpick=0+prev
        #     current=max(pick,notpick)
        #     prev2=prev
        #     prev=current
        # return prev        