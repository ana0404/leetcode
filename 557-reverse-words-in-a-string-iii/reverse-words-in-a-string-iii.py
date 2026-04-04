class Solution:
    def reverseWords(self, s: str) -> str:
        w = s.split()
        def reversestring(w):
            w = list(w)
            left = 0 
            right = len(w)-1
            while left < right:
                w[left],w[right] = w[right],w[left]
                left=left+1
                right=right-1
            return "".join(w)

        res = []
        for c in w:
            res.append(reversestring(c))
        return " ".join(res)

        
                
        