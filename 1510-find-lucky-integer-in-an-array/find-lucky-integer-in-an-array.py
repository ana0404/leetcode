class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        for i in arr:
            freq[i] = freq.get(i,0)+1
        lucky = -1
        for k,val in freq.items():
            if k == val:
                lucky = max(k,lucky)
        return lucky
        