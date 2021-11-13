"""
Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

 

Example 1:

Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Example 2:

Input: words = ["cat","dog","catdog"]
Output: ["catdog"]
 

Constraints:

1 <= words.length <= 104
0 <= words[i].length <= 1000
words[i] consists of only lowercase English letters.
0 <= sum(words[i].length) <= 105
"""
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        def canCompose(word_set, word):
            if len(word) == 0: return False
            
            word_set.remove(word)
            
            dp = (len(word)+1) * [False]
            dp[0] = True
            
            for i in range(1, len(word) + 1):
                for j in range(0, i):
                    if dp[j] == True and word[j:i] in word_set:
                        dp[i] = True
                        break
            
            word_set.add(word) 
            return dp[-1]
        
        
        word_set = set(words)
        ans = []
        for word in words:
            if canCompose(word_set, word):
                ans.append(word)
        
        return ans