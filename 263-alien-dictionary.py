"""
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you.
You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of 
this new language. Derive the order of letters in this language.

You may assume all letters are in lowercase.
The dictionary is invalid, if a is prefix of b and b is appear before a.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return the smallest in normal lexicographical order

Example 1:
Input：["wrt","wrf","er","ett","rftt"]
Output："wertf"
Explanation：
from "wrt"and"wrf" ,we can get 't'<'f'
from "wrt"and"er" ,we can get 'w'<'e'
from "er"and"ett" ,we can get 'r'<'t'
from "ett"and"rftt" ,we can get 'e'<'r'
So return "wertf"

Example 2:
Input：["z","x"]
Output："zx"
Explanation：
from "z" and "x"，we can get 'z' < 'x'
So return "zx"

"""
import heapq
import collections
class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        indegree = {char: 0 for word in words for char in word}
        adjList = collections.defaultdict(list)
        
        for i in range(1, len(words)):
            minLen = min(len(words[i-1]), len(words[i]))
            j = 0
            while j < minLen:
                if words[i-1][j] != words[i][j]:
                    break
                j += 1
            
            if j < minLen:
                adjList[words[i-1][j]].append(words[i][j])
                indegree[words[i][j]] += 1
            elif len(words[i-1]) > len(words[i]):
                return ""
        
        ans = []
        heap = [key for key in indegree if indegree[key] == 0]
        heapq.heapify(heap)
        while len(heap) > 0:
            currLetter = heapq.heappop(heap)
            ans.append(currLetter)

            for nextLetter in adjList[currLetter]:
                indegree[nextLetter] -= 1
                if indegree[nextLetter] == 0:
                    heapq.heappush(heap, nextLetter)

        return "".join(ans) if len(ans) == len(indegree) else ""

