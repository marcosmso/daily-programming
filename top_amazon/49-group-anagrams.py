""" Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically
using all the original letters exactly once.
 
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
 
Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if len(strs) == 0:
            return [[]]
        groups = {}
        
        for s in strs:
            countTuple = self.countLetter(s)
            if countTuple in groups:
                groups[countTuple].append(s)
            else:
                groups[countTuple] = [s]
        
        ans = []
        for group in groups.values():
            ans.append(group)
        return ans
            
    def countLetter(self, s):
        countLetters = 26*[0]
        for char in s:
            countLetters[ord('a')- ord(char)] += 1
        return tuple(countLetters)
            