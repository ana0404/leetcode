class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        arr = []
        for i in range(len(nums)):
            s = nums[i]*nums[i]
            arr.append(s)
        return sorted(arr)
                    