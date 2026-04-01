from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefixes = [1] * len(nums)
        suffixes = [1] * len(nums)

        for i in range(1, len(nums)):
            prefixes[i] = prefixes[i-1] * nums[i-1]

        for j in range(len(nums)-2, -1, -1):
            suffixes[j] = suffixes[j+1] * nums[j+1]

        print(nums)
        # prefixes.reverse()
        # suffixes.reverse()
        print(prefixes)
        print(suffixes)
        output = [a * b for a, b in zip(prefixes, suffixes)]  

        return output