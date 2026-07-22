class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict_count = {}
        hashset = set()
        for i in arr:
            dict_count[i] = dict_count.get(i,0)+1

        if len(dict_count.values()) == len(set(dict_count.values())):
            return True
        else:
            return False         
        