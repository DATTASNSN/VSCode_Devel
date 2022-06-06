'''
Link - https://leetcode.com/problems/3sum/

15. 3Sum 

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []

'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        if len(nums) < 3:
            return []
        else:
            nums = sorted(nums)
            c=[]
            
            for i in range(len(nums)-2):
                if i>0  and nums[i] == nums[i-1]:
                    continue
                first = i+1
                last = len(nums)-1
                while first < last:
                    three_sum = nums[i] + nums[first] + nums[last]
                    if three_sum > target:
                        last-=1
                    elif three_sum < target:
                        first+=1
                    else:
                        c.append([nums[i], nums[first], nums[last]])
                        first+=1
                        while nums[first] == nums[first-1] and first< last:
                            first+=1
            return c  
            # O(n^3) Solution
            # c = []
            # for i in range(len(nums)-2):
            #     for j in range(i+1,len(nums)-1):
            #         for z in range(j+1,len(nums)):
            #             if nums[i]+nums[j]+nums[z] == 0:
            #                 k = [nums[i],nums[j],nums[z]]
            #                 if k not in c:
            #                     c.append(k)
            #                 break
            # return c  
        
        
        