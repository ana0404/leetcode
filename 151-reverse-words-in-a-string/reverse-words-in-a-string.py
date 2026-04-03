class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        words = s.split()
        for i in range(len(words)-1,-1,-1):
            res.append(words[i])
            if i != 0:
                res.append(" ")
        return "".join(res)