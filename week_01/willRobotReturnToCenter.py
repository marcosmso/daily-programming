""" This question is asked by Amazon. Given a string representing the sequence of
moves a robot vacuum makes, return whether or not it will return to its original 
position. The string will only contain L, R, U, and D characters, representing left,
right, up, and down respectively.

Ex: Given the following strings...

"LR", return true
"URURD", return false
"RUULLDRD", return true
"""

from collections import Counter
import unittest

class Solution:
    def willReturnToCenter(self, moves):
        counter = Counter(moves)
        return counter['L'] == counter['R'] and counter["U"] == counter["D"]
        
    # def willReturnToCenter(self, moves):
        
    #     horizontalPos, verticalPos = 0, 0
        
    #     for move in moves:
    #         if move == 'R':
    #             horizontalPos+=1
    #             continue
    #         if move == 'L':
    #              horizontalPos-=1
    #              continue
    #         if move == 'U':
    #             verticalPos +=1
    #             continue
    #         if move == 'D':
    #             verticalPos -=1
        
    #     return horizontalPos == 0 and verticalPos 

class TestSum(unittest.TestCase):

    def test_for_finishing_in_center_moving_only_in_horizontal_axis(self):
        self.assertEqual(Solution().willReturnToCenter("LR"), True)

    def test_for_not_finishing_in_center(self):
        self.assertEqual(Solution().willReturnToCenter("URURD"), False)

    def test_for_finishing_in_center(self):
        self.assertEqual(Solution().willReturnToCenter("RUULLDRD"), True)

if __name__ == "__main__":
    unittest.main()