class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counts = {}
        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in counts:
                return sorted([i, counts[difference]])
            
            if nums[i] not in counts:
                counts[nums[i]] = i
            