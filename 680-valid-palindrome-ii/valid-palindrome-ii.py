class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        left = 0 
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                skipl , skipr = s[left+1 : right+1] , s[left:right]
                return (skipl == skipl[::-1] or skipr == skipr[::-1])
                
            left += 1
            right -= 1
        return True



        