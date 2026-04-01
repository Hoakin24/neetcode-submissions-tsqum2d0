from collections import Counter
from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        output = []

        heap = []
        for num, freq in counts.items():
            heappush(heap, (freq, num))

            if len(heap) > k:
                heappop(heap)

        for item in heap:
            output.append(item[1])
        

        return output
