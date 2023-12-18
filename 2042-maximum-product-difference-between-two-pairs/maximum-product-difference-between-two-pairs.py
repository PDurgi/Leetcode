class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        #brute force => selecting the largest two and smallest two numbers
        #returning their difference
        #we can also solve this using sort but that increases time complexity
        large1,large2=0,0
        small1,small2=float('inf'),float('inf')
        for n in nums:
            if n>large2:
                if n>large1:
                    large2=large1
                    large1=n
                else:
                    large2=n
            if n<small2:
                    if n<small1:
                        small2=small1
                        small1=n    
                    else:
                        small2=n
        return (large1*large2) - (small1*small2)
            


