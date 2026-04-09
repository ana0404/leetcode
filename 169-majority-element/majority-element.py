class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for n in nums:
            dic[n] = dic.get(n,0) + 1
        for i, count in dic.items():
            if dic[i] > len(nums)//2:
                return i

        

        