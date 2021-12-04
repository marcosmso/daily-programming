"""
Given an integer array nums, return the maximum difference between two successive elements in its sorted form. 
If the array contains less than two elements, return 0.
You must write an algorithm that runs in linear time and uses linear extra space.

Example 1:
Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the 
maximum difference 3.

Example 2:
Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
 
Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
"""
class Solution(object):
    def maximumGap(self, nums):
        
        def countingSort(nums, exp):
            
            buckets = [list() for i in range(10)]
            
            for num in nums:
                i = (num // exp) % 10
                buckets[i].append(num)
            
            ans = []
            for bucketList in buckets:
                for num in bucketList:
                    ans.append(num)
            
            return ans
        
        def radixSort(nums):
            max_num = max(nums)
            
            exp = 1
            while max_num / exp > 0:
                nums = countingSort(nums, exp)
                exp *= 10
                
            return nums
        
        if len(nums) < 2:
            return 0
        
        nums = radixSort(nums)
        max_diff = 0
        for i in range(1, len(nums)):
            max_diff = max(max_diff, nums[i]-nums[i-1])
        
        return max_diff
                