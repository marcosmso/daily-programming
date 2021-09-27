"""
This question is asked by Microsoft. Given a string, return the index of its first unique character. 
If a unique character does not exist, return -1.

Ex: Given the following strings...

"abcabd", return 2
"thedailybyte", return 1
"developer", return 0
"""

import unittest
import collections

class Solution:
    def firstUniqueChar(self, s):
        counter = collections.Counter(s)

        for i in range(len(s)):
            if counter[s[i]] == 1:
                return i

        return -1

class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().firstUniqueChar("abcabd"), 2)
    
    def test_2(self):
        self.assertEqual(Solution().firstUniqueChar("thedailybyte"), 1)

    def test_3(self):
        self.assertEqual(Solution().firstUniqueChar("developer"), 0)

    def test_string_with_no_unique_characters(self):
        self.assertEqual(Solution().firstUniqueChar("ddevvelloopperr"), -1)

if __name__ == "__main__":
    unittest.main()