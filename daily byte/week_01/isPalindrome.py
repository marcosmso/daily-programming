  
"""
This question is asked by Facebook. Given a string, return whether or not it forms a palindrome ignoring case and non-alphabetical characters.
Note: a palindrome is a sequence of characters that reads the same forwards and backwards.
Ex: Given the following strings...
    "level", return true
    "algorithm", return false
    "A man, a plan, a canal: Panama.", return true
"""
import unittest

class Solution:
    def isPalindrome(self, string):
        if not string or string == "":
            return True

        i, j = 0, len(string) - 1
        string = string.lower()

        while i != j:
            if not string[i].isalpha():
                i+=1
                continue
            if not string[j].isalpha():
                j-=1
                continue

            if string[i] != string[j]:
                return False
            i += 1
            j -= 1
        
        return True

class TestSum(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(Solution().isPalindrome(""), True)
    
    def test_string_with_one_character(self):
        self.assertEqual(Solution().isPalindrome("c"), True)
    
    def test_string_with_only_spaces(self):
        self.assertEqual(Solution().isPalindrome("   "), True)

    def test_string_with_only_numbers(self):
        self.assertEqual(Solution().isPalindrome("11234223"), True)
    
    def test_palindrome_word_with_numbers_and_letters(self):
        self.assertEqual(Solution().isPalindrome("a112a4223a"), True)

    def test_palindrome_string_with_all_lower_case(self):
        self.assertEqual(Solution().isPalindrome("wordrow"), True)
    
    def test_palindrome_string_with_lower_and_upper_case(self):
        self.assertEqual(Solution().isPalindrome("LevEl"), True)

    def test_not_palindrome_string(self):
        self.assertEqual(Solution().isPalindrome("Algorithnm"), False)

    def test_not_palindrome_with_spaces_and_not_alpha_characters(self):
        self.assertEqual(Solution().isPalindrome("A man, a plan, a canal: Panama."), True)       
        
if __name__ == '__main__':
    unittest.main()