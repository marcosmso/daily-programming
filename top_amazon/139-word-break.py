"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into
 a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.

"""
class Solution:
    def wordBreak(self, target: str, wordDict: List[str]) -> bool:
#         memo = {}
        
#         def helper():
#             if target in memo:
#                 return memo[target]
            
#             if target == "":
#                 return True
 
#             for word in wordDict:
#                 size = len(word)
#                 if target[0:size] == word:
#                     if self.wordBreak(target[size:], wordDict):
#                         memo[target] = True
#                         return True
            
#             memo[target] = False
#             return False
        
#         return helper()
        dp = (len(target)+1)*[False]
        dp[0] = True
        
        for i in range(len(target)+1):
            if not dp[i]: continue 
            for word in wordDict:
                if target[i:i+len(word)] == word:
                    dp[i+len(word)] = True
            
        return dp[-1]
        