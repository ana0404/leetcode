class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = k * threshold
        count = 0
        curr_sum = 0
        for i in range(k):
            curr_sum += arr[i]
        if curr_sum >= target:
            count += 1 

        for i in range(k,len(arr)):
            curr_sum += arr[i]
            curr_sum -= arr[i-k]
            if curr_sum >= target:
                count += 1 

        return count

