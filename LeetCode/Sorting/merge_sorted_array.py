# https://leetcode.com/problems/merge-sorted-array/submissions/


from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        count=0
        for i in range(len(nums1)):
            if nums1[i]==0 and count < len(nums2):
                nums1[i] = nums2[count]
                count+=1
        for j in range(len(nums1)):
            for z in range(j,len(nums1)):
                if nums1[j] > nums1[z]:
                    nums1[j],nums1[z] = nums1[z],nums1[j]
        
        