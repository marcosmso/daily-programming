"""
Given n non-negative integers representing an elevation map
where the width of each bar is 1, compute how much water it can trap after raining.
"""
import unittest

class Solution:
    def trappingRainWater(self, height):
        if not height or len(height) == 0: return 0

        maxLeft, maxRight = 0, 0
        i, j = 0, len(height) - 1
        trappedWater = 0

        while i < j:
            if height[i] < height[j]:
                if height[i] >= maxLeft:
                    maxLeft = height[i]
                else:
                    trappedWater = trappedWater + (maxLeft - height[i])
                i+=1
            else:
                if height[j] >= maxRight:
                    maxRight = height[j]
                else:
                    trappedWater = trappedWater + (maxRight - height[j])
                j-=1
        
        return trappedWater


class Tests(unittest.TestCase):
    def teste_1(self):
        self.assertEqual(Solution().trappingRainWater(None), 0)

    def teste_2(self):
        self.assertEqual(Solution().trappingRainWater([]), 0)

    def teste_3(self):
        self.assertEqual(Solution().trappingRainWater([0,1,0,2,1,0,1,3,2,1,2,1]), 6)

    def teste_4(self):
        self.assertEqual(Solution().trappingRainWater([4,2,0,3,2,5]), 9)

if __name__ == '__main__':
    unittest.main()