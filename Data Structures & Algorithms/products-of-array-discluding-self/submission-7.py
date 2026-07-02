class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefixes = [1, 2, 8, 48]
        # suffixes = [48, 24, 6, 1]
        left = []
        right = [1 for _ in range(len(nums))]


        for i in range(len(nums)):
            if i == 0:
                left.append(1)
            elif i == 1:
                left.append(nums[i-1])
            else:
                left.append(nums[i-1]*left[i-1])


        for j in range(len(nums)-1, -1, -1):
            if j == len(nums)-1:
                right[j] = 1
            elif j == len(nums)-2:
                right[j] = nums[j+1]
            else:
                right[j] = nums[j+1] * right[j+1]
        ans = [x * y for x, y in zip(left, right)]
        return ans


        
      