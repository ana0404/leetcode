class Solution:
    def maxVowels(self, s: str, k: int) -> int: 
        vowels = {'a','e','i','o','u'}
        curr_count = 0
        for i in range(k):
            if s[i] in vowels:
                curr_count += 1
        max_vowels = curr_count
        for i in range(k,len(s)):
            if s[i] in vowels:
                curr_count +=1
            if s[i-k] in vowels:
                curr_count -=1

            max_vowels = max(max_vowels,curr_count)
        return max_vowels

        