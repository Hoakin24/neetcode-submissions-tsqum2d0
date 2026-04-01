from itertools import groupby
from operator import itemgetter

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lst = sorted(set(nums))
        longest = 0
        for k, g in groupby(enumerate(lst), lambda t: t[0] - t[1]):
            group_length = len(list(g))
            if group_length > longest:
                print('reac')
                longest = group_length
        
        return longest