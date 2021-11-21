"""
A wonderful string is a string where at most one letter appears an odd number of times.

For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
Given a string word that consists of the first ten lowercase English letters ('a' through 'j'),
return the number of wonderful non-empty substrings in word. If the same substring appears multiple 
times in word, then count each occurrence separately.

A substring is a contiguous sequence of characters in a string.

Example 1:
Input: word = "aba"
Output: 4
Explanation: The four wonderful substrings are underlined below:
- "aba" -> "a"
- "aba" -> "b"
- "aba" -> "a"
- "aba" -> "aba"

Example 2:
Input: word = "aabb"
Output: 9
Explanation: The nine wonderful substrings are underlined below:
- "aabb" -> "a"
- "aabb" -> "aa"
- "aabb" -> "aab"
- "aabb" -> "aabb"
- "aabb" -> "a"
- "aabb" -> "abb"
- "aabb" -> "b"
- "aabb" -> "bb"
- "aabb" -> "b"

Example 3:
Input: word = "he"
Output: 2
Explanation: The two wonderful substrings are underlined below:
- "he" -> "h"
- "he" -> "e"
 
Constraints:

1 <= word.length <= 105
word consists of lowercase English letters from 'a' to 'j'.
"""
# time, space: O(n), O(n)
import collections
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        if not word or len(word) == 0:
            return 0
        
        states_frequencies = collections.defaultdict(int)
        states_frequencies[0] = 1
        mask = 0
        count = 0
        
        for char in word: #O(11 * n)
            mask = mask ^ (1 << (ord(char)-ord('a')))
            count += states_frequencies[mask]
            
            for i in range(10):
                search_for = mask ^ (1 << i)
                count += states_frequencies[search_for]
            
            states_frequencies[mask] += 1
        
        return count
  
    
    