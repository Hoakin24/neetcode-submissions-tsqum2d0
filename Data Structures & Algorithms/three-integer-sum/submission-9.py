class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sorted_nums = sorted(nums)
        # nums_len = len(nums)
        # outputs = []

        # for i in range(nums_len):
        #     if sorted_nums[i] > 0:
        #         break

        #     if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
        #         continue

        #     left = i + 1
        #     right = nums_len - 1
            
        #     while left < right:
        #         current_total = sorted_nums[left] + sorted_nums[right] + sorted_nums[i]
        #         if current_total < 0:
        #             left += 1
        #         elif current_total > 0:
        #             right -= 1
        #         else:
        #             outputs.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
        #             left += 1
        #             right -= 1
                
        #             while left < right and sorted_nums[left] == sorted_nums[left - 1]:
        #                 left += 1

        #             while left < right and sorted_nums[right] == sorted_nums[right + 1]:
        #                 right -= 1 

        # return outputs


        sorted_nums = sorted(nums)
        nums_len = len(nums)
        outputs = []

        for i in range(nums_len):
            if sorted_nums[i] > 0:
                break
            
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            left = i + 1
            right = nums_len - 1

            while left < right:
                current_total = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]

                if current_total < 0:
                    left += 1
                elif current_total > 0:
                    right -= 1
                else:
                    outputs.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    left += 1
                    right -= 1

                    while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                        left += 1

                    while left < right and sorted_nums[right] == sorted_nums[right + 1]:
                        right -= 1


        return outputs

