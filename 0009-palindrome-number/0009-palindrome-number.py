class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse=0
        val=x
        while(x>0):
            mod=x%10
            reverse=reverse*10 + mod
            x=x//10
        return reverse==val