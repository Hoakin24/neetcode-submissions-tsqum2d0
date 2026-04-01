class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while start != end:
            current_total = numbers[start] + numbers[end]
            if current_total < target:
                start += 1
                continue
            elif current_total > target:
                end -= 1
                continue

            if current_total == target:
                return [start+1, end+1]
            
        # pointer at start and end
        # start checking last going down
        # if last bigger than target, decrease last pointer index
        # if start index + last index bigger

        return []