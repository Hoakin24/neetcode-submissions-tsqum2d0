from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            if i == 0:
                output.append(prod(nums[i+1:len(nums)]))
                print("here in 0")
            else:
                left_side = prod(nums[0:i])
                right_side = prod(nums[i+1:len(nums)])
                output.append(left_side * right_side)
                print("   ")
                print(left_side)
                print(nums[0:i-1])
                print(right_side)
                print(nums[i+1:len(nums)])

        return output