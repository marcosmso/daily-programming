"""
This question is asked by Google. Given a string, return whether or not it uses capitalization correctly. 
A string correctly uses capitalization if all letters are capitalized, no letters are capitalized, or only 
the first letter is capitalized.

Ex: Given the following strings...

"USA", return true
"Calvin", return true
"compUter", return false
"coding", return true
"""

import unittest

class Solution:
    def isCorrectCapitalized(self, string):
        lowerLetters = 0
        
        for char in string:
            if ord('a') <= ord(char) <= ord('z'):
                lowerLetters += 1

        if lowerLetters == 0 or lowerLetters == len(string):
            return True
        
        if lowerLetters == len(string) - 1 and ord('A') <= ord(string[0]) <= ord('Z'):
            return True
        
        return False
        

class Test(unittest.TestCase):
    def test_all_letters_uppercase(self):
        self.assertEqual(Solution().isCorrectCapitalized("USA"), True)

    def test_just_first_letter_uppercase(self):
        self.assertEqual(Solution().isCorrectCapitalized("Calvin"), True)
    
    def test_all_letters_lowercase(self):
        self.assertEqual(Solution().isCorrectCapitalized("listen"), True)
    
    def test_random_letters_uppercase(self):
        self.assertEqual(Solution().isCorrectCapitalized("listEnIng"), False)

if __name__ == "__main__":
    unittest.main()


