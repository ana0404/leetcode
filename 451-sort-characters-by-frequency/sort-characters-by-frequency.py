class Solution:
    def frequencySort(self, s: str) -> str:
        dict_count = {}

        for c in s:
            dict_count[c] = dict_count.get(c,0)+1

        sorted_chars = sorted(dict_count.items(),key = lambda x : x[1], reverse = True)

        result = []
        for char, count in sorted_chars:
            result.append(char*count)
        return "".join(result)
           

        