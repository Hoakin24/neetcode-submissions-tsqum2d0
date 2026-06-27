from collections import OrderedDict, Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        val = []
        for num in range(k):
            res = max(counts, key=counts.get)
            val.append(res)
            del counts[res]
            print(res)
        return val
        # od = OrderedDict(sorted(Counter(nums).items()))
        # print(od)
        # print(list(od))
        # od_list = list(od)
        # return od_list[-k:]