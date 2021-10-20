"""
Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

Example 1:
Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.

Example 2:
Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.
 
Constraints:

1 <= s.length <= 5 * 104
0 <= k <= 50

"""
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or len(s) == 0 or k == 0: 
            return 0 
        
        longest = 0
        counter = defaultdict(int)
        
        def seenLetters():
            seen = 0
            for value in counter.values():
                if value > 0:
                    seen += 1
            return seen
        
        
        i, j = 0, 0 
        while j < len(s):
            letter = s[j]
            
            if counter[letter] > 0 or seenLetters() < k:
                counter[letter] += 1
                longest = max(longest, j-i+1)
                j += 1
                continue
            
            while seenLetters() == k:
                counter[s[i]] -= 1
                i += 1
            
        return longest    