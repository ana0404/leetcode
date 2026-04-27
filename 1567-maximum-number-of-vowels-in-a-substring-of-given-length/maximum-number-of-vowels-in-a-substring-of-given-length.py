class Solution:
    def maxVowels(self, s: str, k: int) -> int: 
        vowels = {'a','e','i','o','u'}
        curr_count = 0
        res = 0
        l = 0
        
        for r in range (len(s)):
            curr_count += 1 if s[r] in vowels else 0
            if r-l+1 > k:
                curr_count -= 1 if s[l] in vowels else 0
                l += 1
            res = max(res,curr_count)
        return res
        