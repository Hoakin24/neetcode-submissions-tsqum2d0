from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = {}
        for s in strs:
            sorted_string = "".join(sorted(s))
            group_name = tuple(Counter(sorted_string).items())
            if group_name in groupings:
                groupings[group_name].append(s)
            else:
                groupings[group_name] = [s]
        return list(groupings.values())
        