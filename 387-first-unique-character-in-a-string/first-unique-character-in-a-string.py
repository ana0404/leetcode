class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict_count = {}
        for c in s:
            dict_count[c] = dict_count.get(c,0)+1
        for i, j in enumerate(s):
            if dict_count[j] == 1:
                return i
        return -1 

