"""
This question is asked by Microsoft. Given an array of strings, return the longest common prefix that is shared amongst all strings.
Note: you may assume all strings only contain lowercase alphabetical characters.

Ex: Given the following arrays...

["colorado", "color", "cold"], return "col"
["a", "b", "c"], return ""
["spot", "spotty", "spotted"], return "spot"

"""
import unittest

class Solution:
    def longestCommonPreffix(self, strs):

        curr_preffix = strs[0]

        for i in range(1, len(strs)):  
            preffix = ""
            for ch1, ch2 in zip(curr_preffix, strs[i]):
                if ch1 != ch2: break
                preffix = preffix + ch1
            curr_preffix = preffix
        
        return curr_preffix
                
    # def longestCommonPreffix(self, strs):

    #     if len(strs) == 0: return ""
        
    #     def countCommonPreffix(str1, str2):
    #         if len(str1) == 0 or len(str2) == 0:
    #             return 0
            
    #         commonChars = 0
    #         for char1, char2 in zip(str1, str2):
    #             if char1 != char2:
    #                 break
    #             commonChars += 1
            
    #         return commonChars
        
    #     maxCommon = float('inf')
    #     for i in range(len(strs) - 1):
    #         maxCommon = min(maxCommon, countCommonPreffix(strs[i], strs[i+1]))
        
    #     return strs[0][0:maxCommon]

class Test(unittest.TestCase):
    def test_strings_have_intersection(self):
        self.assertEqual(Solution().longestCommonPreffix(["colorado", "color", "cold"]), "col")

    def test_strings_have_not_intersection(self):
        self.assertEqual(Solution().longestCommonPreffix(["a", "b", "c"]), "")
    
    def test_one_string_is_empty(self):
        self.assertEqual(Solution().longestCommonPreffix(["colorado", "color", "cold", ""]), "")
    
    def test_intersection_is_the_size_of_smaller_string(self):
        self.assertEqual(Solution().longestCommonPreffix(["spot", "spotty", "spotted"]), "spot")

if __name__ == "__main__":
    unittest.main()