# https://leetcode.com/problems/maximum-subarray/submissions/

# Your input
# [-2,1,-3,4,-1,2,1,-5,4]
# stdout
# -2
# 1
# 1
# 4
# 4
# 5
# 6
# 6
# 6



from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxValue = -2147483648
        currentValue = 0
        for i in range(len(nums)):
            currentValue += nums[i]
            maxValue = max(maxValue, currentValue)
            print(maxValue)
            if(currentValue < 0):
                currentValue = 0
        return maxValue
    #my code 200/209 passed
    # result_max = -2147483648
#         for i in range(len(nums)):
#             temp_max=-2147483648
#             for j in range(i+1,len(nums)+1):
#                 temp_sum = sum(nums[i:j])
#                 if temp_sum > temp_max:
#                     temp_max = temp_sum
#             if result_max < temp_max:
#                 result_max = temp_max
#         return result_max