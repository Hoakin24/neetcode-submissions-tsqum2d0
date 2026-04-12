class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        most_volume = 0

        while left < right:
            smaller = min(heights[left], heights[right])
            distance = right - left
            current_volume = smaller * distance

            most_volume = max(current_volume, most_volume)
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else: 
                left += 1
                right -= 1

        return most_volume