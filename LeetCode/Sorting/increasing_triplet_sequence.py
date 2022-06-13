'''
Link - https://leetcode.com/problems/increasing-triplet-subsequence/


334. Increasing Triplet Subsequence
Medium

3956

219

Add to List

Share
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
'''

#My Solution

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        if len(nums_set) <= 2:
            return False
        if nums.index(max(nums))==0 and nums.count(max(nums))==1 :
            return False
        s = None
        i=0
        length = len(nums)
        while i < length:
            if nums[i]!=s:
                s=nums[i]
                i+=1
            else:
                del nums[i]
                length-=1
        for ind,num in enumerate(nums):
            temp_nums = nums[ind:]
            if temp_nums.index(max(temp_nums)) == 0:
                continue
            else:
                temp_nums = nums[ind+1:]
            count=0
            minimum_index = 0
           
            while len(temp_nums)>=1:
                minimum = min(temp_nums)
                minimum_index = temp_nums.index(minimum)
                if minimum <= num:
                    temp_nums.remove(temp_nums[minimum_index])
                elif minimum > num:
                    temp_nums = temp_nums[minimum_index+1:]
                    num = minimum
                    count+=1
                if count==2:
                    return True
        return False

# Optimal Solution O(N)

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float("inf")
        second = float("inf")
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False