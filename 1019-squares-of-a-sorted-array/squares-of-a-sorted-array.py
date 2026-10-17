class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
       n = len(nums)
       result = [0]*n
       l = 0
       r = n-1
       pos = n-1

       while l<=r:
        if abs(nums[l]) > abs(nums[r]):
            result[pos] = nums[l]**2
            l = l+1
        else:
            result[pos] = nums[r]**2
            r=r-1
        pos = pos-1
       return result 

