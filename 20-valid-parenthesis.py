"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true
 
Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
from collections import deque

class Solution:
    def isValid(self, s):
        if s == "":
            return True
        
        mapping = {')':'(', '}':'{', ']':'[' }
        
        stack = deque()
        
        for character in s:
            if character not in mapping:
                stack.append(character)
            else:
                if len(stack) == 0:
                    return False
                topOfStack = stack.pop()
                if mapping[character] != topOfStack:
                    return False    
        return not stack
            