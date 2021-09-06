""" 
This question is asked by Google. Given two integer arrays, return their intersection.
Note: the intersection is the set of elements that are common to both arrays.

Ex: Given the following arrays...

nums1 = [2, 4, 4, 2], nums2 = [2, 4], return [2, 4]
nums1 = [1, 2, 3, 3], nums2 = [3, 3], return [3]
nums1 = [2, 4, 6, 8], nums2 = [1, 3, 5, 7], return []
"""

import unittest

class Solution:
    def getArraysIntersection(self, nums1, nums2):
        if not nums1 or not nums2 or len(nums1) == 0 or len(nums2) == 0:
            return []
        
        set_nums1 = set(nums1)
        intersection = []
        for num in nums2:
            if num not in set_nums1:
                continue
            intersection.append(num)
            set_nums1.remove(num)
        
        return intersection

class Tests(unittest.TestCase):
    def test_arrays_have_intersection(self):
        self.assertEqual(Solution().getArraysIntersection([2, 4, 4, 2], [2, 4]), [2, 4])
    
    def test_arrays_have_intersection_of_a_repeated_element(self):
        self.assertEqual(Solution().getArraysIntersection([1, 2, 3, 3], [3, 3]), [3])
    
    def test_arrays_have_no_intersection(self):
        self.assertEqual(Solution().getArraysIntersection([2, 4, 6, 8], [1, 3, 5, 7]), [])

    def test_one_array_is_empty(self):
        self.assertEqual(Solution().getArraysIntersection([2, 4, 6, 8], []), [])
    
    def test_one_array_is_none(self):
        self.assertEqual(Solution().getArraysIntersection([2, 4, 6, 8], None), [])

if __name__ == '__main__':
    unittest.main()
