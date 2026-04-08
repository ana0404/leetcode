class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for i, c in enumerate(s):
            if count[c] == 1:
               return i
        return -1 
        