class Solution:
    def reverseString(self, s: List[str]) -> None:
        temp = []
        for c in range(len(s)-1,-1,-1):
            temp.append(s[c])
        s[:] = temp 

        
        