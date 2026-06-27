from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums)+1)]
        count = Counter(nums)
        ans = []
        for num in count:
            bucket[count[num]].append(num)

        for i in range(len(nums), 0, -1):
            for num in bucket[i]:
                if len(ans) < k:
                    ans.append(num) 
        return ans