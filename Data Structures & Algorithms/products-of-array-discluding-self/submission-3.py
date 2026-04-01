from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefixes = []
        suffixes = [1] * len(nums)

        for i in range(len(nums)):
            prefixes.append(prod(nums[i+1:]))
        
        for i in range(len(nums)-1, -1, -1):
            suffixes[i] *= prod(nums[:i])

        print(prefixes)
        print(suffixes)
        output = [a * b for a, b in zip(prefixes, suffixes)]  

        return output