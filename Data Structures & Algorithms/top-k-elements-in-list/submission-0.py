from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict(Counter(nums))
        output = []

        i = 0
        while True:
            highest_occurence = max(counts, key=counts.get)
            output.append(highest_occurence)
            del counts[highest_occurence]
            i += 1
            if i == k:
                break

        return output