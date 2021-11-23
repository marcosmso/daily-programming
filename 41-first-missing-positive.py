"""
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

Example 1:
Input: nums = [1,2,0]
Output: 3

Example 2:
Input: nums = [3,4,-1,1]
Output: 2

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if num <= 0:
                nums[i] = len(nums)+1
                
        for i in range(len(nums)):
            curr = abs(nums[i])
            if curr > len(nums):
                continue
            if nums[curr-1] > 0:
                nums[curr-1] = (-1) * nums[curr-1]
            
        for i, num in enumerate(nums):
            if num > 0:
                return i+1
        return len(nums) + 1