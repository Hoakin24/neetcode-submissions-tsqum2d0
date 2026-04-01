class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        for num in nums:
            if not num in counts:
                counts[num] = 1
            elif counts[num]:
                counts[num] += 1
                if counts[num] > 1:
                    return True

        
        return False