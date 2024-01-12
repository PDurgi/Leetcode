class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mid = len(s) // 2
        vowels = set('aeiouAEIOU')
        first_half, second_half = 0, 0
        
        for i in range(0, mid):
            if s[i] in vowels:
                first_half+= 1
        
        for i in range(mid, len(s)):
            if s[i] in vowels:
                second_half += 1
        
        return first_half == second_half
