class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        #brute-force
        # pos_stack,neg_stack=[],[]
        # res=[]
        # for a in nums:
        #     if a < 0:
        #         neg_stack.append(a)
        #     else:
        #         pos_stack.append(a)
        
        # for i in range(len(nums)):
        #     if len(pos_stack)!=0:
        #          res.append(pos_stack.pop(0))
        #     if len(neg_stack)!=0:
        #         res.append(neg_stack.pop(0))
        # return res
        #better approach with extra memory but less time with indices
        i,j=0,1
        res=[0]*len(nums)
        for k in range(0,len(nums)):
            if nums[k]>0:
                res[i]=nums[k]
                i=i+2
            else:
                res[j]=nums[k]
                j=j+2
        return res