"""
This question is asked by Facebook. Given two strings s and t return whether or not s is an anagram of t.
Note: An anagram is a word formed by reordering the letters of another word.

Ex: Given the following strings...

s = "cat", t = "tac", return true
s = "listen", t = "silent", return true
s = "program", t = "function", return false
"""

import unittest

class Solution:
    def isAnagramPair(self, s, t):
        if len(s) != len(t):
            return False

        s, t = s.lower(), t.lower()
        counter = 26 * [0]

        for letter in s:
            counter[ord(letter) - ord('a')] += 1
        
        for letter in t:
            counter[ord(letter) - ord('a')] -= 1

        return counter == 26*[0]

class Test(unittest.TestCase):
    def test_strings_of_different_sizes(self):
        self.assertEqual(Solution().isAnagramPair("arroz", "rrozaa"), False)

    def test_not_valid_string_with_same_size(self):
        self.assertEqual(Solution().isAnagramPair("program", "functio"), False)
    
    def test_valid_pair_of_strings(self):
        self.assertEqual(Solution().isAnagramPair("listen", "silent"), True)
    
    def test_valid_string_with_different_cases(self):
        self.assertEqual(Solution().isAnagramPair("listEn", "silenT"), True)

if __name__ == "__main__":
    unittest.main()