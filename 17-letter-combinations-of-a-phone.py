"""
Given a string containing digits from 2-9 inclusive, return all possible letter 
combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]
 
Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = []
        letters = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w","x", "y", "z"]  
        } 
        
        def backtracking(path=[], index=0):
            
            if len(path) == len(digits):
                combinations.append("".join(path))
                return
            
            possibleLetters = letters[digits[index]]
            for letter in possibleLetters:
                path.append(letter)
                backtracking(path, index+1)
                path.pop()
        
        if digits and len(digits) > 0:
            backtracking()
            
        return combinations