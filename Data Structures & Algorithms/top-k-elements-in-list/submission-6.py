from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums)+1)]
        count = Counter(nums)
        ans = []
        for num in count:
            print(num)
            print(count[num])
            print("--")
            bucket[count[num]].append(num)

        print(bucket)
        for i in range(len(nums), 0, -1):
            print("--__")
            for num in bucket[i]:
                if len(ans) < k:
                    ans.append(num) 
            # if len(ans) < k:
                # for num in i:
            #         ans.append(num)
        return ans