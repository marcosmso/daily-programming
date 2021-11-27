"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
 
Constraints:

1 <= n <= 8
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def helper(opened, closed, curr = []):
            nonlocal n
            
            if closed == n and opened == n:
                output.append("".join(curr))
                return
            
            if opened < n: 
                curr.append("(")
                helper(opened + 1, closed, curr) # can open
                curr.pop()

            if opened > closed:
                curr.append(")")
                helper(opened, closed + 1, curr) # can close 
                curr.pop()
                     
        output = []
        helper(0 , 0, [])
        return output