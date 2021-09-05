  
"""
This question is asked by Google. Given a string, reverse all of its characters and return the resulting string.

Ex: Given the following strings...

“Cat”, return “taC”
“The Daily Byte”, return "etyB yliaD ehT”
“civic”, return “civic”
"""
import unittest

class Solution:
    def reverseString(self, string):
        if string == "":
            return ""
        
        string = list(string)

        i, j = 0, len(string) - 1

        while i < j:
            string[i], string[j] = string[j], string[i]
            i, j = i + 1, j - 1
            
        return "".join(string)

class TestSum(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(Solution().reverseString(""), "")

    def test_string_with_spaces(self):
        self.assertEqual(Solution().reverseString("   "), "   ")
    
    def test_string_with_lowercase_letters(self):
        self.assertEqual(Solution().reverseString("civic"), "civic") 
    
    def test_string_with_lower_and_upper_characters_and_spaces(self):
        self.assertEqual(Solution().reverseString("The Daily Byte"), "etyB yliaD ehT")
        
if __name__ == '__main__':
    unittest.main()