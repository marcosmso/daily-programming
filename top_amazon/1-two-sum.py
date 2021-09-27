""" Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity? """

import unittest

class Solution:
	def twoSum(self, nums, target):
		map = {}
		for idx, num in enumerate(nums):
			if num in map:
				return [map[num], idx]
			
			map[target - num] = idx

class Tests(unittest.TestCase):

	def test_1(self):
		self.assertEqual(Solution().twoSum([2,7,11,15], 9), [0,1])

	def test_2(self):
		self.assertEqual(Solution().twoSum([3,2,4], 6), [1,2])

	def test_3(self):
		self.assertEqual(Solution().twoSum([3,3], 6), [0,1])

if __name__ == '__main__':
	unittest.main()