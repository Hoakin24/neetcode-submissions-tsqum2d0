from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefixes = [1] * len(nums)
        suffixes = [1] * len(nums)

        for i in range(1, len(nums)):
            prefixes[i] = prefixes[i-1] * nums[i-1]
            print(f'i {i}')
            print(f'prefixes[i-1] {prefixes[i-1]}')
            print(f'nums[i] {nums[i]}')
            print(f' = prefixes[i] {prefixes[i]}')

            print(" ")
        
        for i in range(len(nums)-2, -1, -1):
            suffixes[i] = suffixes[i+1] * nums[i+1]
            print(f'i {i}')
            print(f'suffixes[i+1] {suffixes[i+1]}')
            print(f'nums[i] {nums[i]}')
            print(f' = suffixes[i] {suffixes[i]}')
            print(" ")

        print(nums)
        # prefixes.reverse()
        # suffixes.reverse()
        print(prefixes)
        print(suffixes)
        output = [a * b for a, b in zip(prefixes, suffixes)]  

        return output