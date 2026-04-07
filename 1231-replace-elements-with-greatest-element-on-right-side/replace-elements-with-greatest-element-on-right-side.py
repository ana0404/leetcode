class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_num = -1
        for i in range(len(arr)-1,-1,-1):
            if arr[i] > right_num:
                arr[i],right_num = right_num,arr[i]
            else:
                arr[i] = right_num
        return arr
            