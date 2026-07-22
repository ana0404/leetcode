class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
    
        for i in range(n - m + 1):          # last valid starting index
            if haystack[i:i+m] == needle:    # compare the window slice
                return i
        return -1
        