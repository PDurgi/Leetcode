import collections


class Solution:
    def frequencySort(self, s: str) -> str:
        str_dict=collections.defaultdict(int)
        freq=collections.defaultdict(list)

        for a in s:
            str_dict[a]+=1
        for key,val in str_dict.items():
            freq[val].append(key)
        
        res=""
        for i in range(len(s),0,-1):
            if i in freq.keys():
                for char in freq[i]:
                    res+=char*i
        
        return res



