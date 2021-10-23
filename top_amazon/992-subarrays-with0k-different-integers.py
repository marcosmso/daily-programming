"""
Given an integer array nums and an integer k, return the number of good subarrays of nums.
A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.


Example 1:
Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

Example 2:
Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
 
Constraints:
1 <= nums.length <= 2 * 104
1 <= nums[i], k <= nums.length
"""

# count subarrays with at most k and at most k-1 elements, then do atMost(k)- atMost(k-1)
import collections
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def atMostK(nums, k):
            count = 0
            left, right = 0, 0
            frequencies = collections.defaultdict(int)

            while right < len(nums):
                frequencies[nums[right]] += 1

                while len(frequencies) > k:
                    frequencies[nums[left]] -= 1
                    if frequencies[nums[left]] == 0:
                        del frequencies[nums[left]]
                    left += 1
                    
                count += right - left + 1
                right += 1
            
            return count
        
        return atMostK(nums, k) - atMostK(nums, k-1)