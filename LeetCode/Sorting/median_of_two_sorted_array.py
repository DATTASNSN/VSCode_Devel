# https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/

class Solution:
  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    nums1 = nums1 + nums2
    for j in range(len(nums1)):
      for z in range(j,len(nums1)):
        if nums1[j] > nums1[z]:
          nums1[j],nums1[z] = nums1[z],nums1[j]
    if len(nums1)%2==0:
      return (nums1[len(nums1)//2] + nums1[len(nums1)//2 - 1])/2
    else:
      return (nums1[len(nums1)//2])