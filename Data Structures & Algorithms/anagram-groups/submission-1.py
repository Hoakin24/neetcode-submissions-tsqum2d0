from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = {}

        for s in strs:
            curr_s = "".join(sorted(s))
            print(s)
            print(curr_s)

            if curr_s not in str_map:
                str_map[curr_s] = [s]
            else: 
                str_map[curr_s].append(s)
        return list(str_map.values())