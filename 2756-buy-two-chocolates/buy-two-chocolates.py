class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        #find the two min elements in one pass and
        #return the difference
        min1=float('inf')
        min2=float('inf')
        for i in prices:
            if i < min2:
                if i<min1:
                    
                    min2=min1
                    min1=i
                else:
                    min2=i
        val= money-(min1+min2)
        return val if val >=0 else money

        